# NB!: run command below in terminal to enable permissions to run this script
# chmod +x "learn-machine-learning-with-sagemaker/my-experiments/chapter01/06_04 - delete extracted contents of model.sh"

EXPERIMENT_TMP_DIR=learn-machine-learning-with-sagemaker/my-experiments/chapter01/tmp

rm -f $EXPERIMENT_TMP_DIR/additional-params.json
rm -f $EXPERIMENT_TMP_DIR/manifest.json
rm -f $EXPERIMENT_TMP_DIR/model_algo-1
rm -f $EXPERIMENT_TMP_DIR/mx-mod-symbol.json
rm -f $EXPERIMENT_TMP_DIR/mx-mod-0000.params

# run command below in terminal to run this script from project root folder
# ./"learn-machine-learning-with-sagemaker/my-experiments/chapter01/06_04 - delete extracted contents of model.sh"