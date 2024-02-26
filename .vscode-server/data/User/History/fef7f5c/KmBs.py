import yaml
from modules.ansible_config import AnsibleConfiguration
import subprocess
from threading import Thread
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
            return output 
        except Exception as e:
            self.logger.error("Cluster creation failed: %s", str(e))
            raise e