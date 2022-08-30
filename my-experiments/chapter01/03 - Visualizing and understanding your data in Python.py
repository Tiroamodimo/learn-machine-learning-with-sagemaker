import pandas as pd
import os
import matplotlib.pyplot as plt

# import data
file_dir = os.path.join('files')
file_name = "management_experience_and_salary.csv"
file_path = os.path.join(file_dir, file_name)
print(f"file path exists: {os.path.exists(file_path)}")

df_all_data = pd.read_csv(file_path)

# inspect data
print(df_all_data.info())
print(df_all_data)

# generate scatter plot
plt.rcParams["figure.figsize"] = (8, 8)
plt.scatter(
    df_all_data['management_experience_months'],
    df_all_data['monthly_salary'])
plt.xlabel('Management Experience (Months)',
           fontsize=18)
plt.ylabel('Monthly Salary (USD)', fontsize=16)
plt.xlim(0, 120)
plt.ylim(0, 2400)

# save plot
figure_fp = os.path.join(file_dir, 'Management Experience (Months) vs Monthly Salary (USD) scatter plot.png')
plt.savefig(figure_fp)
