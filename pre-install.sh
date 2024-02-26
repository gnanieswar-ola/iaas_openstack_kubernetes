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
cd /home/ubuntu

# Install lablabs.rke2 Ansible role
sudo ansible-galaxy role install lablabs.rke2

# Check if the roles directory already exists
if [ ! -d "/home/ubuntu/roles" ]; then
    # Create directory for roles
    sudo mkdir /home/ubuntu/roles

    # Move lablabs.rke2 role to the roles directory
    sudo mv /home/ubuntu/.ansible/roles/lablabs.rke2 /home/ubuntu
fi

# Check if rke2.yml already exists
if [ ! -f "/home/ubuntu/rke2.yml" ]; then
    # Create rke2.yml file with specified content
    cat <<EOT >> /home/ubuntu/rke2.yml
- name: Deploy RKE2
  hosts: all
  become: yes
  roles:
    - role: lablabs.rke2
EOT
fi

# Install kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# Install Helm
curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
sudo apt-get install apt-transport-https --yes
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm -y

