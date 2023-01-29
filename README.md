# Installation process

# Install python3 of any version (3.2, 3.3, 3.8,  3.10, 3.11)

sudo apt update

sudo apt install python3

# Confirm the version of python installed

python3 --version

# If Python3 has already been installed on the system, execute the command below to install pip3

sudo apt-get -y install python3-pip

# Run the code below to Clone the repository to local machine

git clone https://github.com/denishjackson1/webscraping.git

# Switch to website branch

git checkout -m website

# Create a python virtual environment to run the project and activate for use

python3 -m venv env

source env/bin/activate

# Install the packages from requirements.txt

pip install -r requirements.txt

# Run the project

python website.py