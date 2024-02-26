from ansible_config import AnsibleConfiguration

class ClusterCreation:
    def __init__(self, ansible_config):
        self.ansible_config = ansible_config

    def create_cluster(self, cluster_name):
        try:
            # Build Ansible command using configuration
            ansible_command = self.ansible_config.build_ansible_command()

            # Start Ansible playbook
            self.ansible_config.start_ansible_playbook(ansible_command)

            return {'status': 'success', 'message': 'Cluster creation request sent successfully', 'cluster_name': cluster_name}
        except ValueError as e:
            return {'status': 'error', 'message': f'Invalid IP address Format: {str(e)}'}, 400
