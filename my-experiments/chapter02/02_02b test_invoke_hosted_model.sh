# NB!: run command below in terminal to enable permissions to run this script
# chmod +x "learn-machine-learning-with-sagemaker/my-experiments/chapter02/02_02b test_invoke_hosted_model.sh"

SERVE_IP=localhost
curl -d "1" -X POST http://$SERVE_IP:8080/invocations

# run command below in terminal to run this script from project root folder
# ./"learn-machine-learning-with-sagemaker/my-experiments/chapter02/02_02b test_invoke_hosted_model.sh"
