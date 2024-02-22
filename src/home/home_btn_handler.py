from husky_config import HUSKY_CONFIG
from command_executor import execute_command_over_ssh, execute_command_local

C_EXECUTABLE_FOR_BRAKES = "release_brakes r"
C_EXECUTABLE_FOR_PLAY = "release_brakes p"
HUSKY_DUAL_ARM_DRIVER_CMD = "roslaunch husky_ur_bringup husky_dual_ur_bringup.launch"
UR_DUAL_ARM_MOVEIT_CMD = "roslaunch sds04_husky_moveit_config husky_dual_ur_robotiq_2f_85_moveit_planning_execution.launch"
REMOVE_CODEBASE_CMD =  f"echo 'Remove Old Codebase from Server'; rm -r {HUSKY_CONFIG.SERVER_DIRECTORY}"
REPLACE_CODEBASE_CMD = f"echo 'Copying Codebase to Server'; scp -r {HUSKY_CONFIG.CLIENT_DIRECTORY} {HUSKY_CONFIG.SCP_DIRECTORY}"

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
    execute_command_local(REPLACE_CODEBASE_CMD)

def RELEASE_BRAKES_BTN():
    execute_command_over_ssh(C_EXECUTABLE_FOR_BRAKES)

def POLYSCOPE_PLAY_BTN():
    execute_command_over_ssh(C_EXECUTABLE_FOR_PLAY)