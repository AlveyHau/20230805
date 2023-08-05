# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrontEndJshHXc.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

from Custom_Widgets.Widgets import QCustomSlideMenu

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(778, 526)
        MainWindow.setMaximumSize(QSize(780, 530))
        MainWindow.setStyleSheet(u"*{\n"
"background: #fff;\n"
"border: none;\n"
"padding: 0;\n"
"margin: 0;\n"
"}\n"
"\n"
"#leftMenuSubContainer QPushButton{\n"
"text-align: left;\n"
"padding: 5px 10px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMinimumSize(QSize(0, 0))
        self.leftMenuContainer.setMaximumSize(QSize(45, 16777215))
        self.leftMenuContainer.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        font = QFont()
        font.setPointSize(12)
        self.menuBtn.setFont(font)
        icon = QIcon()
        icon.addFile(u"../resources/menuExpandBtn1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 15, 0, 0)
        self.settingsBtn = QPushButton(self.frame_2)
        self.settingsBtn.setObjectName(u"settingsBtn")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.settingsBtn.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u"../resources/settingsBtn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon1)
        self.settingsBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.settingsBtn)

        self.tableBtn = QPushButton(self.frame_2)
        self.tableBtn.setObjectName(u"tableBtn")
        self.tableBtn.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u"../resources/tableBtn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tableBtn.setIcon(icon2)
        self.tableBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.tableBtn)

        self.chartBtn = QPushButton(self.frame_2)
        self.chartBtn.setObjectName(u"chartBtn")
        self.chartBtn.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u"../resources/chartBtn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.chartBtn.setIcon(icon3)
        self.chartBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.chartBtn)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.likeBtn = QPushButton(self.frame_3)
        self.likeBtn.setObjectName(u"likeBtn")
        self.likeBtn.setFont(font1)
        icon4 = QIcon()
        icon4.addFile(u"../resources/likeBtn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.likeBtn.setIcon(icon4)
        self.likeBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.likeBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)

        self.verticalLayout_2.setStretch(2, 2)

        self.verticalLayout.addWidget(self.leftMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setStyleSheet(u"background: #293241; \n"
"border-radius: 5px;")
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.verticalLayout_8 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(9, 15, -1, 12)
        self.closeMoreMenuBtn = QPushButton(self.frame_4)
        self.closeMoreMenuBtn.setObjectName(u"closeMoreMenuBtn")
        self.closeMoreMenuBtn.setMinimumSize(QSize(0, 35))
        self.closeMoreMenuBtn.setFont(font1)
        self.closeMoreMenuBtn.setLayoutDirection(Qt.RightToLeft)
        self.closeMoreMenuBtn.setStyleSheet(u"background-color: #ededed;\n"
"border-radius: 5px;")
        icon5 = QIcon()
        icon5.addFile(u"../resources/closeBtn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeMoreMenuBtn.setIcon(icon5)
        self.closeMoreMenuBtn.setIconSize(QSize(15, 15))

        self.verticalLayout_7.addWidget(self.closeMoreMenuBtn)


        self.verticalLayout_8.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.centerMenuSubContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.textEdit = QTextEdit(self.frame_5)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(140, 16777215))
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(u"	color: #FFE302;")
        self.textEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.textEdit)


        self.verticalLayout_8.addWidget(self.frame_5)


        self.verticalLayout_6.addWidget(self.centerMenuSubContainer)


        self.horizontalLayout.addWidget(self.centerMenuContainer, 0, Qt.AlignLeft)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.mainPages = QStackedWidget(self.mainBodyContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.settingPage = QWidget()
        self.settingPage.setObjectName(u"settingPage")
        self.verticalLayout_10 = QVBoxLayout(self.settingPage)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.settingPageHeader = QFrame(self.settingPage)
        self.settingPageHeader.setObjectName(u"settingPageHeader")
        self.settingPageHeader.setStyleSheet(u"")
        self.settingPageHeader.setFrameShape(QFrame.StyledPanel)
        self.settingPageHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.settingPageHeader)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, -1, -1, -1)
        self.settingsPageLabel = QPushButton(self.settingPageHeader)
        self.settingsPageLabel.setObjectName(u"settingsPageLabel")
        self.settingsPageLabel.setMinimumSize(QSize(270, 50))
        font2 = QFont()
        font2.setPointSize(17)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        self.settingsPageLabel.setFont(font2)
        self.settingsPageLabel.setStyleSheet(u"background: #293241; \n"
"color: #FFE302;\n"
"border-radius: 5px;")
        self.settingsPageLabel.setIcon(icon1)
        self.settingsPageLabel.setIconSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.settingsPageLabel, 0, Qt.AlignLeft)


        self.verticalLayout_10.addWidget(self.settingPageHeader, 0, Qt.AlignLeft|Qt.AlignTop)

        self.settingPageContent = QFrame(self.settingPage)
        self.settingPageContent.setObjectName(u"settingPageContent")
        self.settingPageContent.setStyleSheet(u"")
        self.settingPageContent.setFrameShape(QFrame.StyledPanel)
        self.settingPageContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.settingPageContent)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.sP_topSection = QFrame(self.settingPageContent)
        self.sP_topSection.setObjectName(u"sP_topSection")
        self.sP_topSection.setStyleSheet(u"background: #293241; \n"
"border-radius: 5px;")
        self.sP_topSection.setFrameShape(QFrame.StyledPanel)
        self.sP_topSection.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.sP_topSection)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.sP_tS_in1 = QFrame(self.sP_topSection)
        self.sP_tS_in1.setObjectName(u"sP_tS_in1")
        self.sP_tS_in1.setMaximumSize(QSize(170, 95))
        self.sP_tS_in1.setStyleSheet(u"background-color: #fff;\n"
"border-radius: 5px;")
        self.sP_tS_in1.setFrameShape(QFrame.StyledPanel)
        self.sP_tS_in1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.sP_tS_in1)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.loadTableBtn = QPushButton(self.sP_tS_in1)
        self.loadTableBtn.setObjectName(u"loadTableBtn")
        self.loadTableBtn.setFont(font1)
        self.loadTableBtn.setIcon(icon2)
        self.loadTableBtn.setIconSize(QSize(50, 50))

        self.verticalLayout_15.addWidget(self.loadTableBtn)

        self.loadTable_label = QLabel(self.sP_tS_in1)
        self.loadTable_label.setObjectName(u"loadTable_label")
        self.loadTable_label.setFont(font1)

        self.verticalLayout_15.addWidget(self.loadTable_label, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.sP_tS_in1)

        self.sP_tS_in2 = QFrame(self.sP_topSection)
        self.sP_tS_in2.setObjectName(u"sP_tS_in2")
        self.sP_tS_in2.setMaximumSize(QSize(170, 95))
        self.sP_tS_in2.setStyleSheet(u"background-color: #fff;\n"
"border-radius: 5px;")
        self.sP_tS_in2.setFrameShape(QFrame.StyledPanel)
        self.sP_tS_in2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.sP_tS_in2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.loadChartBtn = QPushButton(self.sP_tS_in2)
        self.loadChartBtn.setObjectName(u"loadChartBtn")
        self.loadChartBtn.setFont(font1)
        self.loadChartBtn.setIcon(icon3)
        self.loadChartBtn.setIconSize(QSize(50, 50))

        self.verticalLayout_14.addWidget(self.loadChartBtn)

        self.loadChart_label = QLabel(self.sP_tS_in2)
        self.loadChart_label.setObjectName(u"loadChart_label")
        self.loadChart_label.setFont(font1)

        self.verticalLayout_14.addWidget(self.loadChart_label, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.sP_tS_in2)


        self.verticalLayout_13.addWidget(self.sP_topSection)

        self.sP_midSection = QFrame(self.settingPageContent)
        self.sP_midSection.setObjectName(u"sP_midSection")
        self.sP_midSection.setStyleSheet(u"background: #293241; \n"
"border-radius: 5px;")
        self.sP_midSection.setFrameShape(QFrame.StyledPanel)
        self.sP_midSection.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.sP_midSection)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.sP_tS_out = QTextEdit(self.sP_midSection)
        self.sP_tS_out.setObjectName(u"sP_tS_out")
        self.sP_tS_out.setMaximumSize(QSize(16777215, 16777215))
        self.sP_tS_out.setFont(font1)
        self.sP_tS_out.setStyleSheet(u"	color: #FFE302;")
        self.sP_tS_out.setReadOnly(True)

        self.verticalLayout_17.addWidget(self.sP_tS_out)


        self.verticalLayout_13.addWidget(self.sP_midSection)

        self.verticalLayout_13.setStretch(1, 2)

        self.verticalLayout_10.addWidget(self.settingPageContent)

        self.verticalLayout_10.setStretch(1, 2)
        self.mainPages.addWidget(self.settingPage)
        self.tablePage = QWidget()
        self.tablePage.setObjectName(u"tablePage")
        self.verticalLayout_11 = QVBoxLayout(self.tablePage)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(9, 0, 0, 0)
        self.tablePageHeader = QFrame(self.tablePage)
        self.tablePageHeader.setObjectName(u"tablePageHeader")
        self.tablePageHeader.setStyleSheet(u"")
        self.tablePageHeader.setFrameShape(QFrame.StyledPanel)
        self.tablePageHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.tablePageHeader)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.tablePageLabel = QPushButton(self.tablePageHeader)
        self.tablePageLabel.setObjectName(u"tablePageLabel")
        self.tablePageLabel.setMinimumSize(QSize(270, 50))
        font3 = QFont()
        font3.setPointSize(17)
        font3.setBold(True)
        self.tablePageLabel.setFont(font3)
        self.tablePageLabel.setStyleSheet(u"background: #293241; \n"
"color: #FFE302;\n"
"border-radius: 5px;")
        self.tablePageLabel.setIcon(icon2)
        self.tablePageLabel.setIconSize(QSize(0, 0))

        self.horizontalLayout_4.addWidget(self.tablePageLabel)


        self.verticalLayout_11.addWidget(self.tablePageHeader, 0, Qt.AlignLeft|Qt.AlignTop)

        self.tablePageContent = QFrame(self.tablePage)
        self.tablePageContent.setObjectName(u"tablePageContent")
        self.tablePageContent.setStyleSheet(u"background: #293241; \n"
"border-radius: 5px;")
        self.tablePageContent.setFrameShape(QFrame.StyledPanel)
        self.tablePageContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.tablePageContent)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(9, -1, -1, -1)
        self.table = QTableWidget(self.tablePageContent)
        if (self.table.columnCount() < 5):
            self.table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.table.rowCount() < 10):
            self.table.setRowCount(10)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.table.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        self.table.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font1);
        self.table.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font1);
        self.table.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font1);
        self.table.setVerticalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font1);
        self.table.setVerticalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font1);
        self.table.setVerticalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font1);
        self.table.setVerticalHeaderItem(7, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font1);
        self.table.setVerticalHeaderItem(8, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font1);
        self.table.setVerticalHeaderItem(9, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table.setItem(0, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table.setItem(0, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table.setItem(1, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table.setItem(1, 1, __qtablewidgetitem18)
        self.table.setObjectName(u"table")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        self.table.setFont(font4)
        self.table.setStyleSheet(u"background:#fff;")

        self.verticalLayout_16.addWidget(self.table)


        self.verticalLayout_11.addWidget(self.tablePageContent)

        self.verticalLayout_11.setStretch(1, 2)
        self.mainPages.addWidget(self.tablePage)
        self.chartPage = QWidget()
        self.chartPage.setObjectName(u"chartPage")
        self.verticalLayout_12 = QVBoxLayout(self.chartPage)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(9, 0, 0, 0)
        self.chartPageHeader = QFrame(self.chartPage)
        self.chartPageHeader.setObjectName(u"chartPageHeader")
        self.chartPageHeader.setFont(font3)
        self.chartPageHeader.setStyleSheet(u"")
        self.chartPageHeader.setFrameShape(QFrame.StyledPanel)
        self.chartPageHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.chartPageHeader)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.chartPageLabel = QPushButton(self.chartPageHeader)
        self.chartPageLabel.setObjectName(u"chartPageLabel")
        self.chartPageLabel.setMinimumSize(QSize(270, 50))
        self.chartPageLabel.setFont(font3)
        self.chartPageLabel.setStyleSheet(u"background: #293241; \n"
"color: #FFE302;\n"
"border-radius: 5px;")
        self.chartPageLabel.setIcon(icon3)
        self.chartPageLabel.setIconSize(QSize(0, 0))

        self.horizontalLayout_5.addWidget(self.chartPageLabel)


        self.verticalLayout_12.addWidget(self.chartPageHeader, 0, Qt.AlignLeft|Qt.AlignTop)

        self.chartPageContent = QFrame(self.chartPage)
        self.chartPageContent.setObjectName(u"chartPageContent")
        self.chartPageContent.setStyleSheet(u"background: #293241; \n"
"border-radius: 5px;")
        self.chartPageContent.setFrameShape(QFrame.StyledPanel)
        self.chartPageContent.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.chartPageContent)

        self.verticalLayout_12.setStretch(1, 2)
        self.mainPages.addWidget(self.chartPage)

        self.verticalLayout_9.addWidget(self.mainPages)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        self.horizontalLayout.setStretch(2, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText("")
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"   Settings", None))
        self.tableBtn.setText(QCoreApplication.translate("MainWindow", u"   Table", None))
        self.chartBtn.setText(QCoreApplication.translate("MainWindow", u"   Chart", None))
        self.likeBtn.setText(QCoreApplication.translate("MainWindow", u"   More Info", None))
        self.closeMoreMenuBtn.setText(QCoreApplication.translate("MainWindow", u"More Info      ", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">This desktop application was <"
                        "/span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">developed by </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:700;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Dr. Hau Lee Cheun</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">(haulc@utar.<br />edu.my)</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:700;\"><br /></p>\n"
"<"
                        "p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">for training demo </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">purposes.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:700;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Free to use and </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">distribute.</span></p></body></html>", None))
        self.settingsPageLabel.setText(QCoreApplication.translate("MainWindow", u"SETTINGS PAGE", None))
        self.loadTableBtn.setText("")
        self.loadTable_label.setText(QCoreApplication.translate("MainWindow", u"Load Table Data", None))
        self.loadChartBtn.setText("")
        self.loadChart_label.setText(QCoreApplication.translate("MainWindow", u"Load Chart Data", None))
        self.sP_tS_out.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This section report whether the data has been successfully loaded.</p></body></html>", None))
        self.tablePageLabel.setText(QCoreApplication.translate("MainWindow", u"TABLE PAGE", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Col1", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Col2", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Col3", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Col4", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Col5", None));
        ___qtablewidgetitem5 = self.table.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Row1", None));
        ___qtablewidgetitem6 = self.table.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Row2", None));
        ___qtablewidgetitem7 = self.table.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Row3", None));
        ___qtablewidgetitem8 = self.table.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Row4", None));
        ___qtablewidgetitem9 = self.table.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Row5", None));
        ___qtablewidgetitem10 = self.table.verticalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Row6", None));
        ___qtablewidgetitem11 = self.table.verticalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Row7", None));
        ___qtablewidgetitem12 = self.table.verticalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Row8", None));
        ___qtablewidgetitem13 = self.table.verticalHeaderItem(8)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Row9", None));
        ___qtablewidgetitem14 = self.table.verticalHeaderItem(9)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Row10", None));

        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        self.table.setSortingEnabled(__sortingEnabled)

        self.chartPageLabel.setText(QCoreApplication.translate("MainWindow", u"CHART PAGE", None))
    # retranslateUi

