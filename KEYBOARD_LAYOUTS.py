# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_KEYBOARD_LAYOUTS.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_A2Window(object):
    def setupUi(self, A2Window):
        A2Window.setObjectName("A2Window")
        A2Window.resize(1155, 841)
        self.centralwidget = QtWidgets.QWidget(A2Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1131, 766))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(1000, 600))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ImportLayout = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ImportLayout.setObjectName("ImportLayout")
        self.gridLayout.addWidget(self.ImportLayout, 0, 0, 1, 1)
        self.ExportLayout = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.ExportLayout.setObjectName("ExportLayout")
        self.gridLayout.addWidget(self.ExportLayout, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        A2Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(A2Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1155, 26))
        self.menubar.setObjectName("menubar")
        A2Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(A2Window)
        self.statusbar.setObjectName("statusbar")
        A2Window.setStatusBar(self.statusbar)

        self.retranslateUi(A2Window)
        QtCore.QMetaObject.connectSlotsByName(A2Window)

    def retranslateUi(self, A2Window):
        _translate = QtCore.QCoreApplication.translate
        A2Window.setWindowTitle(_translate("A2Window", "MainWindow"))
        self.ImportLayout.setText(_translate("A2Window", "Import Keyboard JSON "))
        self.ExportLayout.setText(_translate("A2Window", "Export Keyboard JSON "))
