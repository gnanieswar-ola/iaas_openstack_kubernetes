import subprocess
import logging

class DependencyInstaller:
    def __init__(self):
        # Set up logging
        logging.basicConfig(level=logging.INFO)

    def install_dependencies(self, requirements_file):
        try:
            # Install Python dependencies using pip
            subprocess.run(['pip', 'install', '-r', requirements_file], check=True)
            logging.info("Python dependencies installed successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error installing Python dependencies: {e}")
