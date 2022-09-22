# NB!: run command below in terminal to enable permissions to run this script
# chmod +x "learn-machine-learning-with-sagemaker/my-experiments/chapter02/01_02 Download the training data.sh"

cd /opt/ml/input/data/train
S3_BUCKET="ml-sagemaker-cookbook-bucket"
PREFIX="chapter01"
aws s3 cp s3://$S3_BUCKET/$PREFIX/input/training_data.csv training_data.csv

# run command below in terminal to run this script from project root folder
# ./"learn-machine-learning-with-sagemaker/my-experiments/chapter02/01_02 Download the training data.sh"
