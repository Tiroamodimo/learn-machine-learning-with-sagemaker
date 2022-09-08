# NB!: run command below in terminal to enable permissions to run this script
# chmod +x "learn-machine-learning-with-sagemaker/my-experiments/chapter02/04_01 push_custom_container_image_to_ecr.sh"


# Navigate to the ml-python directory containing our Dockerfile
PYTHON_ML_DIR="/home/letlhogile/Documents/educational_projects/202208_02 ML Sagemaker Cookbook/environment/opt/ml-python"
cd "$PYTHON_ML_DIR"

# get account_id
ACCOUNT_ID=$(aws sts get-caller-identity | jq -r ".Account")
echo $ACCOUNT_ID

# get region
AWS_REGION=$(aws configure get region)
echo $AWS_REGION

# get ECR server url
AWS_ECR_SERVER=$ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

# Authenticate with Amazon ECR so that we can push our Docker container image to an Amazon ECR repository in our account
aws ecr get-login-password --region $AWS_REGION | sudo docker login --username AWS --password-stdin $AWS_ECR_SERVER

# Specify the image name, uri of remote repo and the tag number
IMAGE_NAME=chap02_python
REMOTE_REPO_URI=$AWS_ECR_SERVER/$IMAGE_NAME
TAG=1

# tag a local image, IMAGE_NAME, with version TAG into the repository with uri, TARGE_IMAGE_URI, with version TA:
sudo docker tag $IMAGE_NAME:$TAG $REMOTE_REPO_URI:$TAG

# push image to amazon ECR
sudo docker push $REMOTE_REPO_URI:$TAG

# run command below in terminal to run this script from project root folder
# ./"learn-machine-learning-with-sagemaker/my-experiments/chapter02/04_01 push_custom_container_image_to_ecr.sh"
