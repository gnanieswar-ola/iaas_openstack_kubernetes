import yaml
from threading import Thread
from flask import jsonify, abort, request
import ipaddress
import subprocess

class ClusterCreation:
    def create_cluster(self, cluster_name):
        try:
            # Build Ansible command
            ansible_command = self.build_ansible_command()

            # Start Ansible playbook
            self.start_ansible_playbook(ansible_command)

            return {'status': 'success', 'message': 'Cluster creation request sent successfully', 'cluster_name': cluster_name}
        except ValueError as e:
            return {'status': 'error', 'message': f'Invalid IP address Format: {str(e)}'}, 400
