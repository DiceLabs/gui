import os

def ui_path(filename):
    UI_DIRECTORY = 'ui'
    return os.path.join(UI_DIRECTORY, filename)

def styles_path(filename):
    STYLES_DIRECTORY = 'styles'
    return os.path.join(STYLES_DIRECTORY, filename)

def icon_path(filename):
    ICON_DIRECTORY = 'desk_icon'
    return os.path.join(ICON_DIRECTORY, filename)

CONTROL_UI = ui_path('pid_control.ui')
MAINWINDOW_UI_FILE = ui_path('mainwindow.ui')
STYLESHEET = styles_path("indigo.qss")
ICON = icon_path("robot_icon.jpeg")