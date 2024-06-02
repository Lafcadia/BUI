# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,
    QMetaObject, QRect, Qt)
from PySide6.QtWidgets import (QComboBox, QLineEdit,
    QPushButton, QWidget)
from PySide6.QtGui import QFont

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(353, 225)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.chooser = QPushButton(self.centralwidget)
        self.chooser.setObjectName(u"chooser")
        self.chooser.setGeometry(QRect(10, 20, 331, 41))
        font = QFont()
        font.setPointSize(15)
        self.chooser.setFont(font)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 70, 331, 41))
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 120, 331, 41))
        self.comboBox.setFont(font)
        self.StartStop = QPushButton(self.centralwidget)
        self.StartStop.setObjectName(u"StartStop")
        self.StartStop.setGeometry(QRect(10, 170, 331, 41))
        self.StartStop.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BUI", None))
        self.chooser.setText(QCoreApplication.translate("MainWindow", u"Choose the Directory to Monitor", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seconds per Scan", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Save as tar", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Save as zip", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Save as folder", None))

        self.StartStop.setText(QCoreApplication.translate("MainWindow", u"Start / Stop", None))
    # retranslateUi

