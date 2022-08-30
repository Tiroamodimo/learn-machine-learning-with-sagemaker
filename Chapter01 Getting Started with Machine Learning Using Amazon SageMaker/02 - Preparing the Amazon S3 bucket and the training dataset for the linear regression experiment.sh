# NB!: run command below in terminal to enable permissions to run this script
# chmod +x "learn-machine-learning-with-sagemaker/Chapter01 Getting Started with Machine Learning Using Amazon SageMaker/02 - Preparing the Amazon S3 bucket and the training dataset for the linear regression experiment.sh"

# create bucket
BUCKET_NAME=ml-sagemaker-cookbook-bucket
aws s3 mb s3://$BUCKET_NAME

# run command below in terminal to run this script from project root folder
# ./"learn-machine-learning-with-sagemaker/Chapter01 Getting Started with Machine Learning Using Amazon SageMaker/02 - Preparing the Amazon S3 bucket and the training dataset for the linear regression experiment.sh"