import mxnet
from mxnet import gluon
from json import load as json_load
from json import dumps as json_dumps
from json import dump as json_dump
from os.path import join as os_path_join

import experiment_help_functions

# Load the model from the extracted contents of the zip file
model_json_file_path = os_path_join('tmp', 'mx-mod-symbol.json')
model_params_file_path = os_path_join('tmp', 'mx-mod-0000.params')

with open(model_json_file_path) as json_file:
    sym_json = json_load(json_file)

sym_json_string = json_dumps(sym_json)

model = gluon.nn.SymbolBlock(
    outputs=mxnet.sym.load_json(
        sym_json_string
    ),
    inputs=mxnet.sym.var('data'))

print(f"model type: {type(model)}")

model.load_parameters(
    model_params_file_path,
    allow_missing=True)

# Initialize the model and prepare the local predict function
model.initialize()

# Perform predictions
print(f"prediction result: {experiment_help_functions.mxnet_predict(42, model=model)}")

# Extract the weight and the bias of the linear regression model
weight_and_bias = experiment_help_functions.extract_mxnet_linear_model_weight_and_bias(model)
weight_and_bias = experiment_help_functions.make_dict_numbers_float(weight_and_bias)
print(f"weight_and_bias: {weight_and_bias}")

# save weight_and_bias
weight_and_bias_filepath = os_path_join('files', 'weight_and_bias.json')
with open(weight_and_bias_filepath, "w") as json_file:
    json_dump(weight_and_bias, json_file)


