#!/bin/bash

# Copy root certificate
sudo cp /home/ubuntu/rke2_modules/root.crt /usr/local/share/ca-certificates
sudo update-ca-certificates

# Create necessary directories
sudo mkdir -p /etc/kubernetes
sudo mkdir -p /etc/kubernetes/ssl

# Copy root certificate to SSL directory
sudo cp /home/ubuntu/rke2_modules/root.crt /etc/kubernetes/ssl

# Edit /etc/hosts
sudo sh -c 'echo "10.230.17.51     keycloak.krutrim.internal" >> /etc/hosts'

# Get RKE2 server node token
RKE2_NODE_TOKEN=$(sudo cat /var/lib/rancher/rke2/server/node-token)

# Edit rke2.yaml
sudo tee /etc/rancher/rke2/config.yaml > /dev/null <<EOF
token: "$RKE2_NODE_TOKEN"
kube-api-server-arg:
    - --oidc-ca-file=/etc/kubernetes/ssl/root.crt
    - --oidc-client-id=gatekeeper
    - --oidc-groups-claim=groups
    - --oidc-issuer-url=https://keycloak.krutrim.internal/auth/realms/local
    - --oidc-username-claim=name 
kube-apiserver-extra-mount:
  - "/etc/kubernetes/ssl:/etc/kubernetes/ssl"
EOF

# Restart rke2-server
sudo systemctl restart rke2-server
