import os
import pandas as pd
from sklearn.model_selection import train_test_split

# import data
file_dir = os.path.join('files')
file_name = "management_experience_and_salary.csv"
file_path = os.path.join(file_dir, file_name)
print(f"file path exists: {os.path.exists(file_path)}")

df_all_data = pd.read_csv(file_path)

# inspect data
print(df_all_data.info())

# perform train-test split
X = df_all_data['management_experience_months']
X = X.values
y = df_all_data['monthly_salary'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Ensure that the training dataset has the target column as the first column
df_training_data = pd.DataFrame({'monthly_salary': y_train,
                                 'management_experience_months': X_train})

df_test_data = pd.DataFrame({'monthly_salary': y_test,
                             'management_experience_months': X_test})

print(f"df_training_data:\n{df_training_data.info()}")
print(f"df_training_data:\n{df_training_data}")

try:
    os.mkdir('tmp')
# if file exists
except FileExistsError:
    pass

df_training_data.to_csv(
    'tmp/training_data.csv',
    header=False, index=False)

df_test_data.to_csv(
    'tmp/test_data.csv',
    header=False, index=False)
