import subprocess
from ssh_command_executor import execute_command_over_ssh
from husky_config import HUSKY_CONFIG

HUSKY_DUAL_ARM_DRIVER_CMD = "roslaunch husky_ur_bringup husky_dual_ur_bringup.launch"
UR_DUAL_ARM_MOVEIT_CMD = "roslaunch sds04_husky_moveit_config husky_dual_ur_robotiq_2f_85_moveit_planning_execution.launch"
C_EXECUTABLE_FOR_BRAKES = "release_brakes"
REMOVE_CODEBASE_CMD =  f"sudo rm -r {HUSKY_CONFIG.SERVER_DIRECTORY_AS_SEEN_FROM_SERVER}"
REPLACE_CODEBASE_CMD = ["scp", "-r", HUSKY_CONFIG.CLIENT_DIRECTORY, HUSKY_CONFIG.SERVER_DIRECTORY]

def GO_TO_HOME_PAGE_ONE(home):
    home.stacked_widget.setCurrentIndex(0)

def GO_TO_HOME_PAGE_TWO(home):
    home.stacked_widget.setCurrentIndex(1)

def GO_TO_CONTROL_PAGE(home):
    home.stacked_widget.setCurrentWidget(home.control_page)

def HUSKY_DRIVER_BTN():
    execute_command_over_ssh(HUSKY_DUAL_ARM_DRIVER_CMD)

def MOVEIT_CONFIG_BTN():
    execute_command_over_ssh(UR_DUAL_ARM_MOVEIT_CMD)

def LOAD_CODEBASE_BTN():
    execute_command_over_ssh(REMOVE_CODEBASE_CMD)
    subprocess.Popen([REPLACE_CODEBASE_CMD])

def RELEASE_BRAKES_BTN():
    execute_command_over_ssh(C_EXECUTABLE_FOR_BRAKES)