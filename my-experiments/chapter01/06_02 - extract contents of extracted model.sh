# NB!: run command below in terminal to enable permissions to run this script
# chmod +x "learn-machine-learning-with-sagemaker/my-experiments/chapter01/06_02 - extract contents of extracted model.sh"

EXPERIMENT_TMP_DIR=learn-machine-learning-with-sagemaker/my-experiments/chapter01/tmp
TAR_CONTENTS=$(tar -xzvf $EXPERIMENT_TMP_DIR/model.tar.gz --directory $EXPERIMENT_TMP_DIR)
unzip $TAR_CONTENTS -d $EXPERIMENT_TMP_DIR

# run command below in terminal to run this script from project root folder
# ./"learn-machine-learning-with-sagemaker/my-experiments/chapter01/06_02 - extract contents of extracted model.sh"