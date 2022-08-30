from json import load as json_load
import matplotlib.pyplot as plt
import numpy as np
from os.path import join as os_path_join
import pandas as pd

from experiment_help_functions import manual_predict_mxnet_linear_learner_model

# load weight_and_bias
weight_and_bias_file_path = os_path_join('files', 'weight_and_bias.json')
with open(weight_and_bias_file_path, "r") as json_file:
    weight_and_bias = json_load(json_file)
print(f"weight_and_bias: {weight_and_bias}")

# load all data
all_data_file_path = os_path_join('files', 'management_experience_and_salary.csv')
df_all_data = pd.read_csv(all_data_file_path)
print(f"df_all_data:\n{df_all_data}\n")

# load test data
test_data_file_path = os_path_join('tmp', 'test_data.csv')
df_test = pd.read_csv(test_data_file_path, names=['monthly_salary', 'management_experience_months'])
print(f"df_test:\n{df_test}\n")
X_test = np.array(df_test['management_experience_months'])
y_test = np.array(df_test['monthly_salary'])

print(f"X_test: {X_test}")
print(f"y_test: {y_test}")

# perform sample prediction
sample_prediction = manual_predict_mxnet_linear_learner_model(42, weight_and_bias)
print(f"sample_prediction: {sample_prediction}")

# generate regression line dataframe
regression_line_df = pd.DataFrame(
    list(range(0, 121)),
    columns=['management_experience_months']
)
regression_line_df['monthly_salary'] = manual_predict_mxnet_linear_learner_model(
    regression_line_df['management_experience_months'], weight_and_bias)

print("regression_line_df")
print("---start----")
print(regression_line_df.info())
print(regression_line_df.head(5))
print(regression_line_df.tail(5))
print("---end----\n")

# Generate the visualization of the regression line with the original scatter plot chart
plot_name = 'regression line with Management Experience (Months) vs Monthly Salary (USD) scatter plot.png'
plot_file_path = os_path_join('files', plot_name)

plt.rcParams["figure.figsize"] = (8, 8)
plt.scatter(
    df_all_data.management_experience_months,
    df_all_data.monthly_salary
)
r_line = regression_line_df
plt.plot(r_line['management_experience_months'],
         r_line['monthly_salary'],
         color='red',
         linewidth=3)
plt.xlabel('Management Experience (Months)', fontsize=18)
plt.ylabel('Monthly Salary (USD)', fontsize=16)
plt.xlim(0, 120)
plt.ylim(0, 2400)
plt.savefig(plot_file_path)