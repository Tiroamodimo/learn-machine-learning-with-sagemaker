import boto3
import os.path
import sagemaker
from sagemaker.image_uris import retrieve

import experiment_help_functions

# get prepare variables required for training
try:
    role_arn = sagemaker.get_execution_role()
except ValueError:
    iam = boto3.client('iam')
    role_arn = iam.get_role(RoleName='AmazonSageMaker-ExecutionRole-20210615T144455')['Role']['Arn']

session = sagemaker.Session()
region_name = boto3.Session().region_name

print(f"role_arn: {role_arn}")
print(f"session: {session}")
print(f"region_name: {region_name}")

s3_bucket = 'ml-sagemaker-cookbook-bucket'
prefix = 'chapter01'

training_s3_input_location = f"s3://{s3_bucket}/{prefix}/input/training_data.csv"
training_s3_output_location = f"s3://{s3_bucket}/{prefix}/output/"

# Prepare the S3 Input parameter with content_type="text/csv
train = sagemaker.inputs.TrainingInput(training_s3_input_location, content_type="text/csv")

# Prepare Amazon ECR URI of the Linear Learner
container = retrieve("linear-learner", region_name, "1")
print(f"Amazon ECR URI of the Linear Learner: {container}")

# Initialize the Estimator object
estimator = sagemaker.estimator.Estimator(
    container,
    role_arn,
    instance_count=1,
    instance_type='ml.m5.xlarge',
    output_path=training_s3_output_location,
    sagemaker_session=session)

# Set the hyperparameters of the estimator
estimator.set_hyperparameters(predictor_type='regressor', mini_batch_size=4)

# Execute the training job
estimator.fit({'train': train})

# get details from training job
print(f"training details:\n{estimator.__dict__}")

# Copy the value of estimator.model_data to a variable named model_data
model_data = estimator.model_data
print(f"model_data: {model_data}")

# Copy the value of estimator.image_uri to a variable named model_uri
model_uri = estimator.image_uri
print(f"model_uri: {model_uri}")

# save model_data and model_uri in environment variable file
variables_list = [model_data, model_uri]
env_var_file_lines = [experiment_help_functions.make_env_var_str_for_env_file(i, globals())
                      for i in variables_list]
print(f"env_var_file_lines: {env_var_file_lines}")

env_file_path = os.path.join('files', '.env')
experiment_help_functions.make_text_file_from_string_list(env_var_file_lines, env_file_path)
