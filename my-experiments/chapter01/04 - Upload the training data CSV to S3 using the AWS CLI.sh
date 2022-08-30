# NB!: run command below in terminal to enable permissions to run this script
# chmod +x "learn-machine-learning-with-sagemaker/my-experiments/chapter01/04 - Upload the training data CSV to S3 using the AWS CLI.sh"

BUCKET_NAME=ml-sagemaker-cookbook-bucket
PREFIX=chapter01
TRAINING_DATA_LOCAL_FILE_PATH=learn-machine-learning-with-sagemaker/my-experiments/chapter01/tmp/training_data.csv
TRAINING_DATA_S3_BUCKET_PATH=s3://$BUCKET_NAME/$PREFIX/input/training_data.csv
aws s3 cp $TRAINING_DATA_LOCAL_FILE_PATH $TRAINING_DATA_S3_BUCKET_PATH

# run command below in terminal to run this script from project root folder
# ./"learn-machine-learning-with-sagemaker/my-experiments/chapter01/04 - Upload the training data CSV to S3 using the AWS CLI.sh"
