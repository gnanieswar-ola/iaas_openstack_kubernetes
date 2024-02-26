from cluster_creation import ClusterCreation
from ansible_config import AnsibleConfiguration
import logging
import subprocess

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def execute_shell_script(script_path):
    try:
        # Execute the shell script
        subprocess.run(['bash', script_path], check=True)
        logging.info("Shell script execution completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing shell script: {e}")

def install_dependencies(requirements_file):
    try:
        # Install Python dependencies using pip
        subprocess.run(['pip', 'install', '-r', requirements_file], check=True)
        logging.info("Python dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error installing Python dependencies: {e}")

if __name__ == "__main__":
    # Path to the shell script and requirements file
    pre_install_script_path = "./pre-install.sh"
    requirements_file_path = "./requirements.txt"

    # Execute the shell script
    execute_shell_script(pre_install_script_path)

    # Install Python dependencies
    install_dependencies(requirements_file_path)

    # Instantiate ClusterCreation
    cluster_creator = ClusterCreation('cluster_config.yml')

    # Define cluster name (you might fetch this from somewhere else)
    cluster_name = "my_cluster"

    # Call create_cluster method
    cluster_creator.create_cluster(cluster_name)