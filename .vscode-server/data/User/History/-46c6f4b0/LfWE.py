import subprocess
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def install_dependencies(requirements_file):
    try:
        # Install Python dependencies using pip
        subprocess.run(['pip', 'install', '-r', requirements_file], check=True)
        logging.info("Python dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error installing Python dependencies: {e}")

if __name__ == "__main__":
    requirements_file_path = "requirements.txt"
    install_dependencies(requirements_file_path)
