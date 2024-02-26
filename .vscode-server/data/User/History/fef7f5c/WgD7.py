import yaml
from ansible_config import AnsibleConfiguration
import subprocess
from threading import Thread
from flask import jsonify, abort
import logging
logger = logging.getLogger(__name__)

class ClusterCreation:
    def __init__(self, config_file):
        self.ansible_config = AnsibleConfiguration(config_file)
        self.logger = logging.getLogger(__name__)

    def create_cluster(self, cluster_name):
        try:
            # Build Ansible command
            ansible_command = self.ansible_config.build_ansible_command()

            # Start Ansible playbook
            self.logger.info("Starting Ansible playbook execution for cluster creation...")
            output = self.ansible_config.run_ansible_playbook(ansible_command)

            # Check for successful completion
            if "ERROR" in output.upper():
                raise Exception("Ansible playbook execution failed: " + output)

            # Ansible playbook execution completed successfully
            self.logger.info("Cluster creation completed successfully.")
            return {'status': 'success', 'message': 'Cluster creation request sent successfully', 'cluster_name': cluster_name}
        except Exception as e:
            self.logger.error("Cluster creation failed: %s", str(e))
            return {'status': 'error', 'message': 'Cluster creation failed', 'error': str(e)}
