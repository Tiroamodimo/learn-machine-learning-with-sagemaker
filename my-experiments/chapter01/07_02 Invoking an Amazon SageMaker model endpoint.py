import boto3
from json import loads as json_loads

# load sagemaker-runtime
sagemaker_client = boto3.client('sagemaker-runtime')

# specify endpoint
endpoint = 'linear-learner-python-sm-cookbook'

# set the payload
payload = "42"

# Trigger the SageMaker inference endpoint
response = sagemaker_client.invoke_endpoint(
    EndpointName=endpoint,
    ContentType='text/csv',
    Body=payload)

# Inspect the structure and contents of response
print(f"response:\n{response}\n")

# parse response object to get prediction object
result = json_loads(
    response['Body'].read().decode('utf-8')
)

print(f"result: {result}")

# delete endpoint

# Create a low-level SageMaker service client.
sagemaker_client_2 = boto3.client('sagemaker')

# Delete endpoint configuration
sagemaker_client_2.delete_endpoint(EndpointName=endpoint)
