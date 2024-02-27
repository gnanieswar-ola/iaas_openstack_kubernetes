#!/bin/bash

# Update package list
sudo apt update

# Install Ansible
sudo apt install ansible -y

# Check Ansible version
ansible --version

# Install Python 3 pip
sudo apt install python3-pip -y

# Move to home directory
mkdir -p /home/ubuntu
cd /home/ubuntu

# Install lablabs.rke2 Ansible role
ansible-galaxy role install lablabs.rke2

# Check if the roles directory already exists
if [ ! -d "/home/ubuntu/roles" ]; then
    # Create directory for roles
    sudo mkdir /home/ubuntu/roles

    # Move lablabs.rke2 role to the roles directory
    sudo cp -r /home/ubuntu/.ansible/roles/lablabs.rke2 /home/ubuntu/roles
fi
