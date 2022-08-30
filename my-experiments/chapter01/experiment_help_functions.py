from datetime import datetime
import json
import mxnet
import numbers

dt_fmt = '%Y%m%dT%H%M%S'


def make_env_var_str_for_env_file(variable, global_variables_dict: dict):
    variable_names = [v_name for v_name, v_val in global_variables_dict.items() if v_val == variable]
    var_name = variable_names[-1]
    env_var_str = f"{var_name.upper()}={variable}"
    return env_var_str


def make_text_file_from_string_list(str_list: list, file_name: str):
    file_lines_list = [i + "\n" for i in str_list]
    with open(file_name, "w") as f:
        f.writelines(file_lines_list)
    print(f"successfully written to {file_name}")


def save_sagemaker_model_training_details_to_json(trained_estimator_object):
    object_dict = trained_estimator_object.__dict__

    model_type = object_dict['image_uri'].split('/')[-1].replace(':', '_')
    file_name = f"training_details_{datetime.now().strftime(dt_fmt)}_{model_type}.json"
    with open(file_name, "w") as json_file:
        json.dump(object_dict, json_file)


def mxnet_predict(x, model: mxnet.gluon.block.SymbolBlock):
    return model(mxnet.nd.array([x]))[0].asscalar()


def extract_mxnet_linear_model_weight_and_bias(model: mxnet.gluon.block.SymbolBlock):
    params = model.collect_params()
    weight = params['fc0_weight'].data()[0].asscalar()
    bias = params['fc0_bias'].data()[0].asscalar()

    return {
        "weight": weight,
        "bias": bias
    }


def make_dict_numbers_float(dictionary: dict):
    for key, val in dictionary.items():
        if isinstance(val, numbers.Number):
            dictionary[key] = float(val)

    return dictionary


def manual_predict_mxnet_linear_learner_model(x, weight_and_bias: dict):
    params = weight_and_bias
    prediction = params['weight'] * x + params['bias']
    return prediction
