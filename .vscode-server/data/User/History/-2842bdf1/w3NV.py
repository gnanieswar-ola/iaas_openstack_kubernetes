from modules import ClusterCreation
from modules import ansible_config
from modules import ShellScriptExecutor
from modules import requirements
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # Execute pre-installation tasks
    logger.info("Executing pre-installation tasks...")
    shell_executor = ShellScriptExecutor()
    shell_executor.execute_shell_script("./scripts/pre-install.sh")

    # Install Python dependencies
    logger.info("Installing Python dependencies...")
    requirements.install_dependencies("./scripts/requirements.txt")

    # Create the cluster
    cluster_creator = ClusterCreation('./scripts/cluster_config.yml')
    cluster_name = "my_cluster"
    cluster_creator.create_cluster(cluster_name)
