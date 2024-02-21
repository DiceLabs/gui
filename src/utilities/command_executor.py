import subprocess
from husky_config import HUSKY_CONFIG

def execute_command_over_ssh(launch_command):
    launch_command = f'source ~/.bashrc; source /etc/profile; {launch_command}'
    base_command = [
        "gnome-terminal", "--", "bash", "-c", 
        f"sshpass -p {HUSKY_CONFIG.SSH_PASSWORD} ssh -X {HUSKY_CONFIG.SSH_USER}@{HUSKY_CONFIG.SSH_IP} '{launch_command}';", "bash"
    ]
    subprocess.Popen(base_command)

def execute_command_local(launch_command):
    base_command = [
        "gnome-terminal", "--", "bash", "-c", f"{launch_command}"
    ]
    subprocess.Popen(base_command)