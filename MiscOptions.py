# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '5.MiscOptions.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_W4Window(object):
    def setupUi(self, W4Window):
        W4Window.setObjectName("W4Window")
        W4Window.resize(1665, 1085)
        self.centralwidget = QtWidgets.QWidget(W4Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1641, 1010))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(300, 500))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.L14_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.L14_5.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Georgia Pro Black")
        font.setBold(True)
        font.setWeight(75)
        self.L14_5.setFont(font)
        self.L14_5.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.L14_5.setObjectName("L14_5")
        self.gridLayout.addWidget(self.L14_5, 15, 0, 1, 1)
        self.P11_5 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.P11_5.setMaximumSize(QtCore.QSize(290, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(132, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.P11_5.setPalette(palette)
        self.P11_5.setObjectName("P11_5")
        self.gridLayout.addWidget(self.P11_5, 14, 0, 1, 1)
        self.L11_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.L11_5.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Georgia Pro Black")
        font.setBold(True)
        font.setWeight(75)
        self.L11_5.setFont(font)
        self.L11_5.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.L11_5.setObjectName("L11_5")
        self.gridLayout.addWidget(self.L11_5, 13, 0, 1, 1)
        self.SaveBtn_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Georgia Pro Black")
        font.setBold(True)
        font.setWeight(75)
        self.SaveBtn_5.setFont(font)
        self.SaveBtn_5.setObjectName("SaveBtn_5")
        self.gridLayout.addWidget(self.SaveBtn_5, 26, 0, 1, 1)
        self.P87_5 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.P87_5.setMaximumSize(QtCore.QSize(290, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(132, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.P87_5.setPalette(palette)
        self.P87_5.setObjectName("P87_5")
        self.gridLayout.addWidget(self.P87_5, 24, 0, 1, 1)
        self.P71_5 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.P71_5.setMaximumSize(QtCore.QSize(290, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(132, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.P71_5.setPalette(palette)
        self.P71_5.setObjectName("P71_5")
        self.gridLayout.addWidget(self.P71_5, 22, 0, 1, 1)
        self.P14_5 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.P14_5.setMaximumSize(QtCore.QSize(290, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(132, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.P14_5.setPalette(palette)
        self.P14_5.setObjectName("P14_5")
        self.gridLayout.addWidget(self.P14_5, 16, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 1)
        self.DefaultBtn_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Georgia Pro Black")
        font.setBold(True)
        font.setWeight(75)
        self.DefaultBtn_5.setFont(font)
        self.DefaultBtn_5.setObjectName("DefaultBtn_5")
        self.gridLayout.addWidget(self.DefaultBtn_5, 28, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 25, 0, 1, 1)
        self.L70_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.L70_5.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Georgia Pro Black")
        font.setBold(True)
        font.setWeight(75)
        self.L70_5.setFont(font)
        self.L70_5.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.L70_5.setObjectName("L70_5")
        self.gridLayout.addWidget(self.L70_5, 19, 0, 1, 1)
        self.toolButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton.setStyleSheet("Color:rgb(255, 21, 21)")
        self.toolButton.setCheckable(False)
        self.toolButton.setChecked(False)
        self.toolButton.setAutoRaise(True)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 7, 0, 1, 1)
        self.P70_5 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.P70_5.setMaximumSize(QtCore.QSize(290, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(132, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.P70_5.setPalette(palette)
        self.P70_5.setObjectName("P70_5")
        self.gridLayout.addWidget(self.P70_5, 20, 0, 1, 1)
        self.L45_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.L45_5.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Georgia Pro Black")
        font.setBold(True)
        font.setWeight(75)
        self.L45_5.setFont(font)
        self.L45_5.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.L45_5.setObjectName("L45_5")
        self.gridLayout.addWidget(self.L45_5, 17, 0, 1, 1)
        self.P5_SEARCH = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.P5_SEARCH.setMinimumSize(QtCore.QSize(256, 40))
        self.P5_SEARCH.setMaximumSize(QtCore.QSize(256, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 228, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 228, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(229, 229, 228, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.P5_SEARCH.setPalette(palette)
        self.P5_SEARCH.setObjectName("P5_SEARCH")
        self.gridLayout.addWidget(self.P5_SEARCH, 9, 0, 1, 1)
        self.L71_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.L71_5.setMinimumSize(QtCore.QSize(300, 0))
        self.L71_5.setMaximumSize(QtCore.QSize(180, 40))
        font = QtGui.QFont()
        font.setFamily("Georgia Pro Black")
        font.setBold(True)
        font.setWeight(75)
        self.L71_5.setFont(font)
        self.L71_5.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.L71_5.setObjectName("L71_5")
        self.gridLayout.addWidget(self.L71_5, 21, 0, 1, 1)
        self.L87_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.L87_5.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setFamily("Georgia Pro Black")
        font.setBold(True)
        font.setWeight(75)
        self.L87_5.setFont(font)
        self.L87_5.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.L87_5.setObjectName("L87_5")
        self.gridLayout.addWidget(self.L87_5, 23, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(7, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 27, 0, 1, 1)
        self.P45_5 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.P45_5.setMaximumSize(QtCore.QSize(290, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(132, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(132, 255, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.P45_5.setPalette(palette)
        self.P45_5.setObjectName("P45_5")
        self.gridLayout.addWidget(self.P45_5, 18, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        W4Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(W4Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1665, 26))
        self.menubar.setObjectName("menubar")
        W4Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(W4Window)
        self.statusbar.setObjectName("statusbar")
        W4Window.setStatusBar(self.statusbar)

        self.retranslateUi(W4Window)
        QtCore.QMetaObject.connectSlotsByName(W4Window)

    def retranslateUi(self, W4Window):
        _translate = QtCore.QCoreApplication.translate
        W4Window.setWindowTitle(_translate("W4Window", "MainWindow"))
        self.L14_5.setToolTip(_translate("W4Window", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Default: </span></p><p><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; color:#ce9178;\">^l </span><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; color:#000000;\">Select Entire Line</span></p></body></html>"))
        self.L14_5.setText(_translate("W4Window", "14.5 ^MButton         "))
        self.L11_5.setToolTip(_translate("W4Window", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Default: </span></p><p><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; color:#ce9178;\">^p </span><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; color:#000000;\">Cycle Files In VS_Code/Print in Chrome</span></p></body></html>"))
        self.L11_5.setText(_translate("W4Window", "11.5 +Mbutton"))
        self.SaveBtn_5.setText(_translate("W4Window", "SAVE MISC HOTKEYS"))
        self.DefaultBtn_5.setText(_translate("W4Window", "RESTORE MISC DEFAULTS"))
        self.L70_5.setToolTip(_translate("W4Window", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Default: </span></p><p><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; color:#ce9178;\">^!j </span><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; color:#000000;\">Cycle VS_Code Bookmarks Backward</span></p></body></html>"))
        self.L70_5.setText(_translate("W4Window", "70.5 CapsLock & Z"))
        self.toolButton.setToolTip(_translate("W4Window", "<html><head/><body><p><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; text-decoration: underline; color:#000000;\">KEY:</span></p><p><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; color:#ce9178;\">^:</span><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; color:#000000;\"> CTRL</span></p><p><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; color:#ce9178;\">+:</span><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; color:#000000;\"> Shift</span></p><p><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; color:#ce9178;\">!:</span><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; color:#000000;\"> Alt</span></p><p><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; color:#ce9178;\">#:</span><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; color:#000000;\"> Windows Key</span></p><p><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; color:#ce9178;\">RButton:</span><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; color:#000000;\"> Right Mouse Button</span></p><p><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; color:#ce9178;\">LButton:</span><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; color:#000000;\"> Left Mouse Button</span></p></body></html>"))
        self.toolButton.setText(_translate("W4Window", "?"))
        self.L45_5.setToolTip(_translate("W4Window", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Default: </span></p><p><span style=\" font-family:\'Consolas\',\'Courier New\',\'monospace\'; font-size:11pt; font-weight:600; color:#ce9178;\">!+{F12} </span><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; color:#000000;\">Find All References In Repo</span></p></body></html>"))
        self.L45_5.setText(_translate("W4Window", "45.5 Tab & MButton"))
        self.P5_SEARCH.setPlaceholderText(_translate("W4Window", "Search"))
        self.L71_5.setToolTip(_translate("W4Window", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Default: </span></p><p><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; color:#ce9178;\">^!l </span><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; color:#000000;\">Cycle VS_Code Bookmarks Forward</span></p></body></html>"))
        self.L71_5.setText(_translate("W4Window", "71.5 CapsLock & X"))
        self.L87_5.setToolTip(_translate("W4Window", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Default: </span></p><p><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; color:#ce9178;\">!{LButton} </span><span style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:600; color:#000000;\">Create multiple mouse-cursors in VS_Code</span></p></body></html>"))
        self.L87_5.setText(_translate("W4Window", "87.5 !LButton "))
