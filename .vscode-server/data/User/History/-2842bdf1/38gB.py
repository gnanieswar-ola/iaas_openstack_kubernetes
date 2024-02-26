from modules import cluster_creation
from modules import ansible_config
from modules import pre_install
from modules import requirements
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # Execute pre-installation tasks
    logger.info("Executing pre-installation tasks...")
    shell_executor = pre_install()
    shell_executor.execute_shell_script("./scripts/pre-install.sh")

    # Install Python dependencies
    logger.info("Installing Python dependencies...")
    requirements.requirements("./scripts/requirements.txt")

    # Create the cluster
    cluster_creator = cluster_creation('./scripts/cluster_config.yml')
    cluster_name = "my_cluster"
    cluster_creator.create_cluster(cluster_name)
