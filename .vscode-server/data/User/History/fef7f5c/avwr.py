import yaml
from modules.ansible_config import AnsibleConfiguration
import subprocess
from threading import Thread
from flask import jsonify, abort
import logging
logger = logging.getLogger(__name__)

class ClusterCreation:
    def __init__(self, ansible_config):
        self.ansible_config = ansible_config
        self.logger = logging.getLogger(__name__)

    def create_cluster(self):
        try:
            ansible_command = self.ansible_config.build_ansible_command()
            self.logger.info("Starting Ansible playbook execution for cluster creation...")
            output = self.ansible_config.run_ansible_playbook(ansible_command)
            self.logger.info("Cluster creation completed successfully.")
            return output  # Return the Ansible output for further processing if needed
        except Exception as e:
            self.logger.error("Cluster creation failed: %s", str(e))
            raise e


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