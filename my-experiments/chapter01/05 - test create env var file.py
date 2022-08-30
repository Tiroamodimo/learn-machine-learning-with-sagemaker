import experiment_help_functions

model_data = 'some model data'
model_arn = 'some mode arn text'


variables_list = [model_data, model_arn]
env_var_file_lines = [experiment_help_functions.make_env_var_str_for_env_file(i, globals())
                      for i in variables_list]

print(env_var_file_lines)
