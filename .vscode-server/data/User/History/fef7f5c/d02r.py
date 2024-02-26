from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import ipaddress
import subprocess
from threading import Thread

app = Flask(__name__)
CORS(app)

class ClusterCreation:
    def __init__(self):
        pass

    def build_ansible_command(self, rke2_version, upgrade_required=False):
        try:
            playbook_path = '/home/ubuntu/rke2.yml'
            ansible_command = [
                'ansible-playbook',
                '-i', '/tmp/dynamic_inventory.ini',
                playbook_path,
                '--user', 'ubuntu',
                '--private-key', '/home/ubuntu/privatekey.pem',
                '--ssh-common-args', '-o StrictHostKeyChecking=no'
            ]

            if rke2_version:
                ansible_command.extend(['-e', f'rke2_version={rke2_version}'])
            ansible_command.extend(['-e', f'rke2_drain_node_during_upgrade={upgrade_required}'])

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

    def create_cluster(self, rke2_version, master_ips, worker_ips, cluster_name):
        try:
            master_ips = self.validate_ip_addresses(master_ips)
            worker_ips = self.validate_ip_addresses(worker_ips)

            # Build Ansible command
            ansible_command = self.build_ansible_command(rke2_version)

            # Start Ansible playbook
            self.start_ansible_playbook(ansible_command)

            return jsonify({'status': 'success', 'message': 'Cluster creation request sent successfully', 'cluster_name': cluster_name})
        except ValueError as e:
            return jsonify({'status': 'error', 'message': f'Invalid IP address Format: {str(e)}'}), 400

    def validate_ip_addresses(self, ips):
        try:
            return [str(ipaddress.ip_address(ip)) for ip in ips if ip]
        except ValueError as e:
            raise ValueError(f'Invalid IP address Format: {str(e)}')

cluster_creation = ClusterCreation()

@app.route('/api/cluster/create', methods=['POST'])
def create_cluster_api():
    data = request.json
    rke2_version = data.get('rke2_k8s_version')
    master_ips = data.get('master_ips', [])
    worker_ips = data.get('worker_ips', [])
    cluster_name = data.get('cluster_name')

    if not all([rke2_version, master_ips, cluster_name]):
        return jsonify({'status': 'error', 'message': 'rke2_k8s_version, master_ips, and cluster_name are required attributes'}), 400

    return cluster_creation.create_cluster(rke2_version, master_ips, worker_ips, cluster_name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', use_reloader=False)
