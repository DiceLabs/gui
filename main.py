#!/usr/bin/python3

import sys
import os

def add_program_directories():
    """ 
        Setup Environment
    """
    directories_to_add_to_path = [
        "src", 
        "util",
        "src/home", 
        "src/controller",
        "src/utilities"
    ]
    for directory in directories_to_add_to_path:
        path = os.path.abspath(directory) 
        if path not in sys.path:
            sys.path.append(path)
add_program_directories()

##############################################################################

from PyQt5 import QtWidgets
from home_page import HomePage
from resources import STYLESHEET

READ_MODE  = "r"
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    with open(STYLESHEET, READ_MODE) as fh:
        app.setStyleSheet(fh.read())
    window = HomePage()
    window.show()
    sys.exit(app.exec_())
