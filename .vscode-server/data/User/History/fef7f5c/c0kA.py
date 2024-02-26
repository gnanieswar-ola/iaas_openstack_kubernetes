import yaml
from modules.ansible_config import AnsibleConfiguration
import subprocess
from threading import Thread
from flask import jsonify, abort
import logging
logger = logging.getLogger(__name__)

class ClusterCreation:
    def __init__(self, config_file):
        self.ansible_config = AnsibleConfiguration(config_file)
        self.logger = logging.getLogger(__name__)
        self.ansible_output = None  # Initialize ansible_output to store the output

    def create_cluster(self, cluster_name):
        try:
            ansible_command = self.ansible_config.build_ansible_command()
            self.logger.info("Starting Ansible playbook execution for cluster creation...")
            self.ansible_output = self.ansible_config.run_ansible_playbook(ansible_command)
            if "ERROR" in self.ansible_output.upper():
                raise Exception("Ansible playbook execution failed: " + self.ansible_output)
            self.logger.info("Cluster creation completed successfully.")
        except Exception as e:
            self.logger.error("Cluster creation failed: %s", str(e))
            self.ansible_output = None

# class ClusterCreation:
#     def __init__(self, config_file):
#         self.ansible_config = AnsibleConfiguration(config_file)
#         self.logger = logging.getLogger(__name__)

#     def create_cluster(self, cluster_name):
#         try:
#             ansible_command = self.ansible_config.build_ansible_command()
#             self.logger.info("Starting Ansible playbook execution for cluster creation...")
#             output = self.ansible_config.run_ansible_playbook(ansible_command)
#             if "ERROR" in output.upper():
#                 raise Exception("Ansible playbook execution failed: " + output)
#             self.logger.info("Cluster creation completed successfully.")
#         except Exception as e:
#             self.logger.error("Cluster creation failed: %s", str(e))