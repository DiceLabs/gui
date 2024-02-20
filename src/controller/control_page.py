from PyQt5 import QtWidgets, uic
from resources import CONTROL_UI

class ControlPage(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(CONTROL_UI, self)
