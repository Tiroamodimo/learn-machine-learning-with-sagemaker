# NB!: run command below in terminal to enable permissions to run this script
# chmod +x "learn-machine-learning-with-sagemaker/my-experiments/chapter02/03_01b run_test_serve_container.sh"


# Navigate to the ml-python directory containing our Dockerfile
PYTHON_ML_DIR="/home/letlhogile/Documents/educational_projects/202208_02 ML Sagemaker Cookbook/environment/opt/ml-python"
cd "$PYTHON_ML_DIR"

# Specify the image name and the tag number
IMAGE_NAME=chap02_python
TAG=1

sudo docker run --name pyserve --rm -v /opt/ml:/opt/ml $IMAGE_NAME:$TAG serve

# run command below in terminal to run this script from project root folder
# ./"learn-machine-learning-with-sagemaker/my-experiments/chapter02/03_01b run_test_serve_container.sh"
