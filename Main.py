## 0. IMPORT PACKAGES
import sys
import os
from ui_Main import *
from Custom_Widgets.Widgets import *

from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout)



## 1. MAIN WINDOW CLASS
class MainWindow(QMainWindow):
    def button_pressed(self, btnName):
        if btnName == 'menu':
            self.ui.menuBtn.setStyleSheet("background-color: #ededed;")
            self.ui.settingsBtn.setStyleSheet("background-color: #fff;")
            self.ui.tableBtn.setStyleSheet("background-color: #fff;")
            self.ui.chartBtn.setStyleSheet("background-color: #fff;")
            self.ui.likeBtn.setStyleSheet("background-color: #fff;")
            self.ui.centerMenuContainer.expandMenu()

        elif btnName == 'like':
            self.ui.menuBtn.setStyleSheet("background-color: #fff;")
            self.ui.settingsBtn.setStyleSheet("background-color: #fff;")
            self.ui.tableBtn.setStyleSheet("background-color: #fff;")
            self.ui.chartBtn.setStyleSheet("background-color: #fff;")
            self.ui.likeBtn.setStyleSheet("background-color: #ededed;")

        elif btnName == 'settings':
            self.ui.menuBtn.setStyleSheet("background-color: #fff;")
            self.ui.settingsBtn.setStyleSheet("background-color: #ededed;")
            self.ui.tableBtn.setStyleSheet("background-color: #fff;")
            self.ui.chartBtn.setStyleSheet("background-color: #fff;")
            self.ui.likeBtn.setStyleSheet("background-color: #fff;")

        elif btnName == 'table':
            self.ui.menuBtn.setStyleSheet("background-color: #fff;")
            self.ui.settingsBtn.setStyleSheet("background-color: #fff;")
            self.ui.tableBtn.setStyleSheet("background-color: #ededed;")
            self.ui.chartBtn.setStyleSheet("background-color: #fff;")
            self.ui.likeBtn.setStyleSheet("background-color: #fff;")

        elif btnName == 'chart':
            self.ui.menuBtn.setStyleSheet("background-color: #fff;")
            self.ui.settingsBtn.setStyleSheet("background-color: #fff;")
            self.ui.tableBtn.setStyleSheet("background-color: #fff;")
            self.ui.chartBtn.setStyleSheet("background-color: #ededed;")
            self.ui.likeBtn.setStyleSheet("background-color: #fff;")

    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## APPLY JSON STYLESHEET
        loadJsonStyle(self, self.ui)
        
        ## SHOW WINDOW
        self.show()

        ## EXPAND CENTER MENU WIDGET SIZE
        self.ui.menuBtn.clicked.connect(lambda: self.button_pressed('menu'))
        self.ui.likeBtn.clicked.connect(lambda: self.button_pressed('like')) 
        self.ui.settingsBtn.clicked.connect(lambda: self.button_pressed('settings')) 
        self.ui.tableBtn.clicked.connect(lambda: self.button_pressed('table')) 
        self.ui.chartBtn.clicked.connect(lambda: self.button_pressed('chart')) 
        

        ## CLOSE CENTER MENU WIDGET
        self.ui.closeMoreMenuBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())       



## 2. EXECUTE APP
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.setWindowTitle("Demo App Dev in Python")
    window.setWindowIcon(QIcon("resources/logo.ico"))

    # app.setWindowIcon(QIcon("resources/images/takoIcon.ico"))
 
    window.show()

    sys.exit(app.exec())


