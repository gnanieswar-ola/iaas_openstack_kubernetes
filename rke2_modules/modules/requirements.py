import subprocess
import logging

class DependencyInstaller:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    def install_dependencies(self, requirements_file):
        try:
            subprocess.run(['pip', 'install', '-r', requirements_file], check=True)
            logging.info("Python dependencies installed successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error installing Python dependencies: {e}")
