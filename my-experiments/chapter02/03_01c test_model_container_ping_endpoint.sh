# NB!: run command below in terminal to enable permissions to run this script
# chmod +x "learn-machine-learning-with-sagemaker/my-experiments/chapter02/03_01c test_model_container_ping_endpoint.sh"

# get the IP address of the running Flask app
SERVE_IP=$(sudo docker network inspect bridge | jq -r ".[0].Containers[].IPv4Address" | awk -F/ '{print $1}')
echo $SERVE_IP

# test the ping endpoint URL
sudo curl http://$SERVE_IP:8080/ping

# run command below in terminal to run this script from project root folder
# ./"learn-machine-learning-with-sagemaker/my-experiments/chapter02/03_01c test_model_container_ping_endpoint.sh"
