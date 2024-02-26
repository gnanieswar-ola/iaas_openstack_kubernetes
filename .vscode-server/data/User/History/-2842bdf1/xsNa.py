from modules.cluster_creation import ClusterCreation
from modules.ansible_config import AnsibleConfiguration
from modules.pre_install import execute_shell_script as pre_install_script
from modules.requirements import install_dependencies
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Executing pre-installation tasks...")
    pre_install.execute_shell_script("./scripts/pre-install.sh")

    logger.info("Installing Python dependencies...")
    requirements.install_dependencies("./scripts/requirements.txt")

    cluster_creator = ClusterCreation('./scripts/cluster_config.yml')
    cluster_name = "my_cluster"
    cluster_creator.create_cluster(cluster_name)