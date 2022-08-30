import boto3
from dotenv import load_dotenv
from os.path import join as os_path_join
from os import environ
import sagemaker
from sagemaker import get_execution_role
from sagemaker.model import Model
from sagemaker.predictor import Predictor
from sagemaker.serializers import CSVSerializer
from sagemaker.deserializers import JSONDeserializer

# load environment variable from env file
env_file_path = os_path_join('files', '.env')
load_dotenv(env_file_path)

# import model data and uri
model_data = environ['MODEL_DATA']
model_uri = environ['MODEL_URI']

print(f"model_data: {model_data}")
print(f"model_uri: {model_uri}")

# load sagemaker role
try:
    role = get_execution_role()
except ValueError:
    iam = boto3.client('iam')
    role = iam.get_role(RoleName='AmazonSageMaker-ExecutionRole-20210615T144455')['Role']['Arn']

# load sagemaker session
session = sagemaker.Session()

# initialise sagemaker model object
model = Model(image_uri=model_uri,
              model_data=model_data,
              role=role,
              sagemaker_session=session)

# Set predictor_cls of the model to sagemaker.predictor.Predictor
# If predictor_cls is set, calling the deploy() function in the next step would return a Predictor object
model.predictor_cls = Predictor

# deploy the Linear Learner model to an inference endpoint
predictor = model.deploy(
    initial_instance_count=1,
    instance_type='ml.m5.xlarge',
    endpoint_name="linear-learner-python-sm-cookbook")

# Update the serializer and deserializer configurations of predictor
predictor.serializer = CSVSerializer()
predictor.deserializer = JSONDeserializer()

# perform single sample prediction
sample_single_prediction = predictor.predict("42")
print(f"sample_single_prediction: {sample_single_prediction}")

# perform prediction on to 2 values
sample_double_prediction = predictor.predict(["42", "81"])
print(f"sample_double_prediction: {sample_double_prediction}")

# delete endpoint (commented)
# predictor.delete_endpoint()