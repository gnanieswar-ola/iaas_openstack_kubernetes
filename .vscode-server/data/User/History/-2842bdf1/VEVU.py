from cluster_creation import ClusterCreation
from ansible_config import AnsibleConfiguration
import logging
import pre_install
import requirements

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == "__main__":

    pre_install_script_path = "./pre-install.sh"
    requirements_file_path = "./requirements.txt"

    execute_shell_script(pre_install_script_path)
    install_dependencies(requirements_file_path)

    cluster_creator = ClusterCreation('cluster_config.yml')
    cluster_name = "my_cluster"
    cluster_creator.create_cluster(cluster_name)