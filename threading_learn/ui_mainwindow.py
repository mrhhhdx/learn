# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

#from menubar import menuBar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionFile = QAction(MainWindow)
        self.actionFile.setObjectName(u"actionFile")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QRect(20, 10, 481, 111))
        self.textBrowser.setMouseTracking(True)
        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(320, 150, 121, 16))
        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(70, 150, 91, 21))
        self.checkBox_4.setCheckable(True)
        self.checkBox_4.setChecked(False)
        self.checkBox_4.setAutoRepeat(False)
        self.checkBox_4.setTristate(False)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(False)
        self.groupBox_2.setGeometry(QRect(280, 180, 191, 251))
        self.pushButton_2 = QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 220, 149, 23))
        self.checkBox_8 = QCheckBox(self.groupBox_2)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setGeometry(QRect(10, 50, 149, 16))
        self.checkBox_9 = QCheckBox(self.groupBox_2)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setGeometry(QRect(10, 118, 149, 16))
        self.checkBox_10 = QCheckBox(self.groupBox_2)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setGeometry(QRect(10, 20, 149, 16))
        self.checkBox_11 = QCheckBox(self.groupBox_2)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setGeometry(QRect(10, 152, 149, 16))
        self.checkBox_12 = QCheckBox(self.groupBox_2)
        self.checkBox_12.setObjectName(u"checkBox_12")
        self.checkBox_12.setGeometry(QRect(10, 84, 149, 16))
        self.comboBox_8 = QComboBox(self.groupBox_2)
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setGeometry(QRect(100, 140, 69, 22))
        self.comboBox_7 = QComboBox(self.groupBox_2)
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setGeometry(QRect(100, 110, 69, 22))
        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(100, 20, 69, 22))
        self.comboBox_2 = QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(100, 50, 69, 22))
        self.comboBox_3 = QComboBox(self.groupBox_2)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(100, 80, 69, 22))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(160, 190, 31, 16))
        self.lineEdit_3 = QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(50, 190, 31, 16))
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 190, 31, 16))
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(90, 190, 31, 16))
        self.lineEdit_4 = QLineEdit(self.groupBox_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(120, 190, 31, 16))
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(530, 10, 241, 141))
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 211, 111))
        self.horizontalLayoutWidget = QWidget(self.groupBox_3)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(40, 100, 161, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(False)
        self.groupBox.setGeometry(QRect(20, 180, 201, 251))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 221, 141, 20))
        self.checkBox_6 = QCheckBox(self.groupBox)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(10, 50, 149, 16))
        self.checkBox_5 = QCheckBox(self.groupBox)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(10, 118, 149, 16))
        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(10, 20, 149, 16))
        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 152, 149, 16))
        self.checkBox_7 = QCheckBox(self.groupBox)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QRect(10, 84, 149, 16))
        self.comboBox_9 = QComboBox(self.groupBox)
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setGeometry(QRect(100, 140, 69, 22))
        self.comboBox_10 = QComboBox(self.groupBox)
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setGeometry(QRect(100, 110, 69, 22))
        self.comboBox_11 = QComboBox(self.groupBox)
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.setObjectName(u"comboBox_11")
        self.comboBox_11.setEnabled(False)
        self.comboBox_11.setGeometry(QRect(100, 20, 69, 22))
        self.comboBox_12 = QComboBox(self.groupBox)
        self.comboBox_12.setObjectName(u"comboBox_12")
        self.comboBox_12.setGeometry(QRect(100, 50, 69, 22))
        self.comboBox_13 = QComboBox(self.groupBox)
        self.comboBox_13.setObjectName(u"comboBox_13")
        self.comboBox_13.setGeometry(QRect(100, 80, 69, 22))
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(50, 190, 31, 16))
        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(120, 190, 31, 16))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 190, 31, 16))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 190, 31, 16))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 190, 31, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        '''self.menubar = menuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionOpen)
        self.menuMenu.addAction(self.actionSave)'''

        self.retranslateUi(MainWindow)
        self.checkBox_4.clicked.connect(self.groupBox.setEnabled)
        self.checkBox_3.clicked.connect(self.groupBox_2.setEnabled)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionFile.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Video and Photo", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Normal Photo", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5f55\u50cf\u53c2\u6570", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"SHUTTER", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"WB", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"ISO", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"EV", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5206\u949f", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u65f6", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Version", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u" ROV\uff1a\n"
" RC\uff1a\n"
" WiFi\uff1a\n"
" Camera\uff1a\n"
"", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Get New", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Upgrade", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u62cd\u7167\u53c2\u6570", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"SHUTTER", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"WB", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"ISO", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"EV", None))
        self.comboBox_11.setItemText(0, QCoreApplication.translate("MainWindow", u"100", None))
        self.comboBox_11.setItemText(1, QCoreApplication.translate("MainWindow", u"150", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5206\u949f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5c0f\u65f6", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4\uff1a", None))
        #self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

