#!/bin/bash

# Update and install necessary packages
sudo apt-get update
sudo apt-get install -y \
    git \
    docker.io \
    docker-compose \
    ansible \
    python3 \
    python3-pip

# Start Docker service
sudo systemctl start docker.service

# Add current user to Docker group
sudo usermod -aG docker $USER

# Start Docker Compose service
sudo systemctl start docker-compose.service

# Install pip3 packages
sudo pip3 install \
    ansible-lint \
    molecule \
    docker \
    docker-compose

echo "Current directory: $(pwd)" 
git clone https://github.com/Samay1993/dockerCompose-Ansible-Terraform-Ubuntu.git

# Run Ansible playbook
cd dockerCompose-Ansible-Terraform-Ubuntu/ansible
sudo ansible-playbook playbook.yaml -i hosts
