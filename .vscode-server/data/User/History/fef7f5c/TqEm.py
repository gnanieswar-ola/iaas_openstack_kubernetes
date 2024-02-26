import yaml
from ansible_config import AnsibleConfiguration
import subprocess
from threading import Thread
from flask import jsonify, abort

class ClusterCreation:
    def __init__(self):
        self.ansible_config = AnsibleConfiguration('config.yml')

    def create_cluster(self, cluster_name):
        try:
            # Build Ansible command
            ansible_command = self.ansible_config.build_ansible_command()

            # Run Ansible playbook directly
            output = self.ansible_config.run_ansible_playbook(ansible_command)

            # Check for errors in the output
            if 'error' in output.lower():
                return {'status': 'error', 'message': output, 'cluster_name': cluster_name}
            else:
                return {'status': 'success', 'message': 'Cluster creation request sent successfully', 'cluster_name': cluster_name}
        except Exception as e:
            return {'status': 'error', 'message': f'Error creating cluster: {str(e)}'}, 500
