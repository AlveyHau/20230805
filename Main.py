## 0. IMPORT PACKAGES
import sys
import os
from ui_Main import *
from Custom_Widgets.Widgets import *

from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout)



# import pandas # import pandas library
# import csv # import csv module in Python


## IMPORT PYSIDE
# from PySide2.QtGui import QPainter
# from PySide2.QtCharts import QtCharts




# globals()[f'imgPath_dictionary'] = {'structurePicture': "resources/images/no-image.png",
#                                     'servicePicture_S1': "resources/images/no-image.png",
#                                     'servicePicture_S2': "resources/images/no-image.png",
#                                     'zonePicture_Z1': "resources/images/no-image.png",
#                                     'zonePicture_Z2': "resources/images/no-image.png",
#                                     'zonePicture_Z3': "resources/images/no-image.png",
#                                     'zonePicture_Z4': "resources/images/no-image.png",
#                                     'zonePicture_Z5': "resources/images/no-image.png"}








## 1. MAIN WINDOW CLASS
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## APPLY JSON STYLESHEET
        loadJsonStyle(self, self.ui)
        
        ## SHOW WINDOW
        self.show()





    ### SAVE IMAGE TO DEFAULT PICTURE
    # def setImage_toDefault(self, image_name):
    #     default_pixmap = QPixmap("resources/images/no-image.png")
    #     widget = getattr(self.ui, image_name, None)
    #     widget.setPixmap(default_pixmap.scaledToWidth(widget.width()))   






    ## OPEN CUSTOM SETTINGS (JSON FILE)
    # def openCustom_Settings(self):

    #     ### PROMPT USER TO CHOOSE THE SPECIFIC CUSTOM SETTINGS FILE (.JSON) TO OPEN
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog

    #     settings_path = ""
    #     file_dialog = QFileDialog()
    #     file_dialog.setWindowTitle("Open Custom Settings")
    #     file_dialog.setDirectory("custom settings")
    #     file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
    #     file_dialog.setFileMode(QFileDialog.AnyFile)
    #     file_dialog.setNameFilter("JSON Files (*.json)")
    #     file_dialog.setOptions(options)
    #     file_dialog.setDefaultSuffix("json")
    #     file_dialog.selectFile(settings_path)

    #     result = file_dialog.exec()

    #     if result == QFileDialog.Accepted:
    #         # Change cursor to loading symbol
    #         QApplication.setOverrideCursor(Qt.WaitCursor)

    #         settings_path = file_dialog.selectedFiles()[0]

    #         ### LOAD CUSTOM SETTINGS FROM THE SELECTED FILE
    #         with open(settings_path, "r") as f:
    #             custom_settings = json.load(f)

    



    # ### OPEN IMAGE AND SAVE THE FILE PATH
    # # def open_image(self, image_name):
    # #     options = QFileDialog.Options()
    # #     options |= QFileDialog.DontUseNativeDialog
    # #     image_path, _ = QFileDialog.getOpenFileName(
    # #         None, 
    # #         "Select Image: PNG or JPG only", 
    # #         "dummy images", #! TBDeleted 20230721
    # #         "Image Files (*.png *.jpg)", 
    # #         options=options)
    # #     if image_path:
    # #         pixmap = QPixmap(image_path)
    # #         widget = getattr(self.ui, image_name, None)
    # #         widget.setPixmap(pixmap.scaledToWidth(widget.width()))

    # #         temp = image_path.replace('/', '\\')
    # #         globals()[f'imgPath_dictionary'][image_name] = temp














    #     self.ui.defaultBtn.clicked.connect(lambda: self.checkCenterMenu('update'))

    #     ## CLOSE CENTER MENU WIDGET
    #     self.ui.generalBtn.clicked.connect(lambda: self.checkCenterMenu('collapse')) 









## 2. EXECUTE APP
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    # window.setWindowTitle("TAKO Lightning Risk Assessment Software")
    # window.setWindowIcon(QIcon("resources/images/takoIcon.ico"))


    # app.setWindowIcon(QIcon("resources/images/takoIcon.ico"))
 
    window.show()

    sys.exit(app.exec())


