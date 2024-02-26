import logging
from ansible_config import AnsibleConfiguration
from cluster_creation import ClusterCreation
from pre_install import ShellScriptExecutor
from requirements import DependencyInstaller

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    cluster_config_file = "./scripts/cluster_config.yml"
    pre_install_script_path = "./scripts/pre-install.sh"
    requirements_file_path = "./scripts/requirements.txt"
    
    try:
        logger.info("Executing pre-installation tasks...")
        pre_install_executor = ShellScriptExecutor()
        pre_install_executor.execute_shell_script(pre_install_script_path)

        logger.info("Installing Python dependencies...")
        dependency_installer = DependencyInstaller()
        dependency_installer.install_dependencies(requirements_file_path)

        ansible_config = AnsibleConfiguration(cluster_config_file)
        cluster_creator = ClusterCreation(ansible_config)
        logger.info("Creating the cluster...")
        cluster_creator.create_cluster()

        logger.info("Cluster creation process completed successfully.")

    except Exception as e:
        logger.error(f"Error encountered during cluster creation: {e}")



# from modules.cluster_creation import ClusterCreation
# from modules.ansible_config import AnsibleConfiguration
# from modules.pre_install import ShellScriptExecutor
# from modules.requirements import DependencyInstaller
# import logging

# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

# if __name__ == "__main__":
#     cluster_config_file = "./scripts/cluster_config.yml"
#     pre_install_script_path = "./scripts/pre-install.sh"
#     requirements_file_path = "./scripts/requirements.txt"
#     try:
#         logger.info("Executing pre-installation tasks...")
#         pre_install_executor = ShellScriptExecutor()
#         pre_install_executor.execute_shell_script(pre_install_script_path)

#         logger.info("Installing Python dependencies...")
#         dependency_installer = DependencyInstaller()
#         dependency_installer.install_dependencies(requirements_file_path)

#         logger.info("Creating the cluster...")
#         cluster_creator = ClusterCreation(cluster_config_file)
#         cluster_name = "my_cluster"
#         cluster_creator.create_cluster(cluster_name)

#         logger.info("Cluster creation process completed successfully.")

#     except Exception as e:
#         logger.error(f"Error encountered during cluster creation: {e}")
