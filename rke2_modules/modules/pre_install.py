import subprocess
import logging

class ShellScriptExecutor:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
    def execute_shell_script(self, script_path):
        try:
            subprocess.run(['bash', script_path], check=True)
            logging.info("Shell script execution completed successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error executing shell script: {e}")
