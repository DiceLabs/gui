import home_btn_handler 
from PyQt5 import QtWidgets, uic
from control_page import ControlPage
from resources import MAINWINDOW_UI_FILE

"""
    Available resources from UI
    self.page_forward_btn
    self.page_back_btn
    self.home_page_btn
    self.control_page_btn
    self.husky_driver_btn
    self.load_codebase_btn
    self.moveit_config_btn
    self.release_brakes_bt
"""

class HomePage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(MAINWINDOW_UI_FILE, self)
        self.addPages()
        self.addIcons()
        self.connectButtons()    
        
    def addPages(self):
        self.control_page = ControlPage()
        self.stacked_widget.addWidget(self.control_page)
        home_btn_handler.GO_TO_HOME_PAGE_ONE(self)
    
    def addIcons(self):
        self.page_forward_btn.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_ArrowForward))
        self.page_back_btn.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_ArrowBack))
        self.page_forward_btn.setAutoRaise(True)
        self.page_back_btn.setAutoRaise(True)
        
    def connectButtons(self):
        self.home_page_btn.clicked.connect(lambda: home_btn_handler.GO_TO_HOME_PAGE_ONE(self))
        self.page_back_btn.clicked.connect(lambda: home_btn_handler.GO_TO_HOME_PAGE_ONE(self))
        self.page_forward_btn.clicked.connect(lambda: home_btn_handler.GO_TO_HOME_PAGE_TWO(self))
        self.control_page_btn.clicked.connect(lambda: home_btn_handler.GO_TO_CONTROL_PAGE(self))
        self.husky_driver_btn.clicked.connect(lambda: home_btn_handler.HUSKY_DRIVER_BTN())
        self.load_codebase_btn.clicked.connect(lambda: home_btn_handler.LOAD_CODEBASE_BTN())
        self.moveit_config_btn.clicked.connect(lambda: home_btn_handler.MOVEIT_CONFIG_BTN())
        self.release_brakes_btn.clicked.connect(lambda: home_btn_handler.RELEASE_BRAKES_BTN())

