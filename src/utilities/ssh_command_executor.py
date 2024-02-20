import subprocess
from husky_config import HUSKY_CONFIG

def execute_command_over_ssh(self, launch_command):
    base_command = [
        "gnome-terminal", "--", "bash", "-c", 
        f"sshpass -p {HUSKY_CONFIG.SSH_PASSWORD} ssh -X {HUSKY_CONFIG.SSH_USER}@{HUSKY_CONFIG.HUSKY_IP} '{launch_command}; exec bash'"
    ]
    subprocess.Popen(base_command)