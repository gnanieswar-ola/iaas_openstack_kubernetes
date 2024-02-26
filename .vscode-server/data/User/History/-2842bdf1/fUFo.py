from modules import ClusterCreation
from modules import ansible_config
from modules import pre_install
from modules import requirements
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # Execute pre-installation tasks
    logger.info("Executing pre-installation tasks...")
    try:
        subprocess.run(['bash', './scripts/pre-install.sh'], check=True)
        logger.info("Pre-installation tasks completed successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error executing pre-installation tasks: {e}")

    # Install Python dependencies
    logger.info("Installing Python dependencies...")
    requirements.install_dependencies("./scripts/requirements.txt")

    # Create the cluster
    cluster_creator = ClusterCreation('./scripts/cluster_config.yml')
    cluster_name = "my_cluster"
    cluster_creator.create_cluster(cluster_name)
