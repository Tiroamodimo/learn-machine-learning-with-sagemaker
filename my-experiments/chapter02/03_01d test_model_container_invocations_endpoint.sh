# NB!: run command below in terminal to enable permissions to run this script
# chmod +x "learn-machine-learning-with-sagemaker/my-experiments/chapter02/03_01d test_model_container_invocations_endpoint.sh"

# get the IP address of the running Flask app
SERVE_IP=$(sudo docker network inspect bridge | jq -r ".[0].Containers[].IPv4Address" | awk -F/ '{print $1}')
echo $SERVE_IP

#test the invocations endpoint URL
curl -d "1" -X POST http://$SERVE_IP:8080/invocations

# run command below in terminal to run this script from project root folder
# ./"learn-machine-learning-with-sagemaker/my-experiments/chapter02/03_01d test_model_container_invocations_endpoint.sh"
