from PyQt5 import QtWidgets, uic
from control_page import ControlPage
from resources import MAINWINDOW_UI_FILE

""" Available resources from UI
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
        self.GO_TO_HOME_PAGE_ONE()
        
    def addPages(self):
        self.control_page = ControlPage()
        self.stacked_widget.addWidget(self.control_page)
    
    def addIcons(self):
        self.page_forward_btn.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_ArrowForward))
        self.page_back_btn.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_ArrowBack))
        self.page_forward_btn.setAutoRaise(True)
        self.page_back_btn.setAutoRaise(True)
        
    def connectButtons(self):
        self.home_page_btn.clicked.connect(lambda: self.GO_TO_HOME_PAGE_ONE())
        self.page_back_btn.clicked.connect(lambda: self.GO_TO_HOME_PAGE_ONE())
        self.page_forward_btn.clicked.connect(lambda: self.GO_TO_HOME_PAGE_TWO())
        self.control_page_btn.clicked.connect(lambda: self.GO_TO_CONTROL_PAGE())
        self.husky_driver_btn.clicked.connect(lambda: self.HUSKY_DRIVER_BTN())
        self.load_codebase_btn.clicked.connect(lambda: self.LOAD_CODEBASE_BTN())
        self.moveit_config_btn.clicked.connect(lambda: self.MOVEIT_CONFIG_BTN())
        self.release_brakes_bt.clicked.connect(lambda: self.RELEASE_BRAKES_BTN())

    ####################################### BUTTON FUNCTIONS ########################################

    def GO_TO_HOME_PAGE_ONE(self):
        self.stacked_widget.setCurrentIndex(0)

    def GO_TO_HOME_PAGE_TWO(self):
        self.stacked_widget.setCurrentIndex(1)

    def GO_TO_CONTROL_PAGE(self):
        self.stacked_widget.setCurrentWidget(self.control_page)
    
    def HUSKY_DRIVER_BTN(self):
        pass
    
    def MOVEIT_CONFIG_BTN(self):
        pass
    
    def LOAD_CODEBASE_BTN(self):
        pass

    def RELEASE_BRAKES_BTN(self):
        pass

