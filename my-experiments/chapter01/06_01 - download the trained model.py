from dotenv import load_dotenv
import os.path
import sagemaker
from sagemaker.s3 import S3Downloader

# load environment variable from env file
env_file_path = os.path.join('files', '.env')
load_dotenv(env_file_path)

# Load model_data from environment variables
model_data = os.environ['MODEL_DATA']
print(f"model_data: {model_data}")

# Prepare the SageMaker session
session = sagemaker.Session()

# download the model.tar.gz file from S3 to the tmp directory
S3Downloader.download(s3_uri=model_data,
                      local_path="tmp/",
                      sagemaker_session=session)


