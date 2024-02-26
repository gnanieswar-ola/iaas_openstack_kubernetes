import yaml
from threading import Thread
from flask import jsonify, abort, request
import ipaddress
import subprocess

class ClusterCreation:
    def __init__(self):
        # Load configuration from config.yml
        with open('cluster_config.yml', 'r') as f:
            config = yaml.safe_load(f)
            self.playbook_path = config['playbook_path']
            self.private_key_path = config['private_key_path']
            self.inventory_path = config['inventory_path']
            self.default_user = config['default_user']
            self.rke2_version = config['rke2_version']
            self.upgrade_required = config['upgrade_required']

    def build_ansible_command(self):
        try:
            ansible_command = [
                'ansible-playbook',
                '-i', self.inventory_path,
                self.playbook_path,
                '--user', self.default_user,
                '--private-key', self.private_key_path,
                '--ssh-common-args', '-o StrictHostKeyChecking=no'
            ]

            if self.rke2_version:
                ansible_command.extend(['-e', f'rke2_version={self.rke2_version}'])
            ansible_command.extend(['-e', f'rke2_drain_node_during_upgrade={self.upgrade_required}'])

            return ansible_command
        except Exception as e:
            abort(500, jsonify({'status': 'error', 'message': f'Error building Ansible command: {str(e)}'}))

    def run_ansible_playbook(self, ansible_command):
        try:
            output = subprocess.check_output(ansible_command, stderr=subprocess.STDOUT, text=True)
            return output
        except subprocess.CalledProcessError as e:
            error_message = f'Cluster creation or upgrade failed: {str(e)}'
            if e.output is not None:
                error_message += f'\n{e.output}'
            return error_message

    def start_ansible_playbook(self, ansible_command):
        Thread(target=self.run_ansible_playbook, args=(ansible_command,)).start()

    def create_cluster(self, cluster_name):
        try:
            # Build Ansible command
            ansible_command = self.build_ansible_command()

            # Start Ansible playbook
            self.start_ansible_playbook(ansible_command)

            return {'status': 'success', 'message': 'Cluster creation request sent successfully', 'cluster_name': cluster_name}
        except ValueError as e:
            return {'status': 'error', 'message': f'Invalid IP address Format: {str(e)}'}, 400