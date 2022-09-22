# NB!: run command below in terminal to enable permissions to run this script
# chmod +x "learn-machine-learning-with-sagemaker/Chapter02 Building and Using Your Own Algorithm Container Image/01_01 install and use tree command.sh"

# Navigate to the /opt directory
cd /opt

# Create the /opt/ml directory
sudo mkdir -p ml

# Modify the ownership configuration of the /opt/ml directory
sudo chown $USER ml

# Navigate to the ml directory
cd ml

# prepare the expected directory structure inside the /opt/ml directory
mkdir -p input/config
mkdir -p input/data/train
mkdir -p output/failure
mkdir -p model

# Create a new "opt" directory
PROJECT_DIR="/home/letlhogile/Documents/educational_projects/202208_02 ML Sagemaker Cookbook"
mkdir -p "$PROJECT_DIR/environment/opt"
cd "$PROJECT_DIR/environment/opt"
mkdir -p ml-python ml-r

# Create a soft symbolic link to make it easier to manage the files and directories
sudo ln -s /opt/ml "$PROJECT_DIR/environment/opt/ml"

# run command below in terminal to run this script from project root folder
# ./"learn-machine-learning-with-sagemaker/Chapter02 Building and Using Your Own Algorithm Container Image/01_01 install and use tree command.sh"
