import subprocess
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def execute_shell_script(script_path):
    try:
        # Execute the shell script
        subprocess.run(['bash', script_path], check=True)
        logging.info("Shell script execution completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing shell script: {e}")

if __name__ == "__main__":
    pre_install_script_path = "pre-install.sh"
    execute_shell_script(pre_install_script_path)
