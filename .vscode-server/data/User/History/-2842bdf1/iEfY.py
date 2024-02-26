from cluster_creation import ClusterCreation
from ansible_config import AnsibleConfiguration
import logging
import pre_install
import requirements

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Executing pre-installation tasks...")
    pre_install.execute_shell_script("pre-install.sh")

    # Install Python dependencies
    logger.info("Installing Python dependencies...")
    requirements.install_dependencies("requirements.txt")

    # Instantiate ClusterCreation
    cluster_creator = ClusterCreation('cluster_config.yml')

    # Define cluster name (you might fetch this from somewhere else)
    cluster_name = "my_cluster"

    # Call create_cluster method
    cluster_creator.create_cluster(cluster_name)