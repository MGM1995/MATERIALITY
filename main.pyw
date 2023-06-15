
import resources
from ast import Try
from pickle import TRUE
from shutil import move
import qtmodern.styles
import qtmodern.windows
import sys
import os
import subprocess
import time
import json
from PyQt5.QtGui import QIcon
import MainApp
import GeneralBackend
import PREFRENCES_MENU
import AdobeBackend
import ExcelBackend
import WordBackend
import importlib
import MiscBackend
import subprocess
import FileCallBackend
import ConditionalStringsBackend
from PyQt5 import QtGui
from TitleWindow import Ui_MainWindow
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QDialog, QDialogButtonBox, QVBoxLayout, QSystemTrayIcon,
                             QAction, QMenu, QFileDialog)


app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

FILE_FILTERS = [
    "JSON files (*.json)"
]


font = QtGui.QFont()
font.setFamily("Georgia Pro Black")



basedir = os.path.dirname(__file__)
icon = QtGui.QIcon(":/icons/front.png")



class Window(QMainWindow, Ui_MainWindow):
    SaveConfirmed = 0
    GenWindow = GeneralBackend.GeneralOptionsBackend()
    AdobeWindow = AdobeBackend.AdobeOptionsBackend()
    ExcelWindow = ExcelBackend.ExcelOptionsBackend()
    WordWindow = WordBackend.WordOptionsBackend()
    MiscWindow = MiscBackend.MiscOptionsBackend()
    FileCallWindow = FileCallBackend.FileCallsOptionsBackend()
    PrefrencesWindow = PREFRENCES_MENU.TOGGLE_OPTIONS()
    ConditionalWindow = ConditionalStringsBackend.ConditionalStringsOptionsBackend()
    RestoreDefaults = 0

    def __init__(self, *args, obj=None, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Materiality")
        self.setWindowIcon(icon)

        self.Toggle.stateChanged.connect(self.change_state)

        self.GeneralOptions.clicked.connect(self.GeneralOptionsWindow)
        self.AdobeOptions.clicked.connect(self.AdobeOptionsWindow)
        self.ExcelOptions.clicked.connect(self.ExcelOptionsWindow)
        self.WordOptions.clicked.connect(self.WordOptionsWindow)
        self.MiscOptions.clicked.connect(self.MiscOptionsWindow)
        self.FileCallOptions.clicked.connect(self.FileCallsOptionsWindow)
        self.RESTORE_DEFAULTS_BTN.clicked.connect(self.Restore_All_Defaults)
        self.PREFRENCES_ACTION.triggered.connect(self.OPEN_PREFRENCES)
        self.CONDITIONAL_ACTION.triggered.connect(self.OPEN_CONDITIONAL)

        self.ExportLayout.triggered.connect(self.ExportKeyboardLayout)
        self.ImportLayout.triggered.connect(self.ImportKeyboardLayout)

        self.WordWindow.SaveSignal.connect(self.tray_restart)
        self.AdobeWindow.SaveSignal.connect(self.tray_restart)
        self.ExcelWindow.SaveSignal.connect(self.tray_restart)
        self.GenWindow.SaveSignal.connect(self.tray_restart)
        self.MiscWindow.SaveSignal.connect(self.tray_restart)
        self.ConditionalWindow.SaveSignal.connect(self.tray_restart)
        self.FileCallWindow.SaveSignal.connect(self.tray_restart)
        self.ConditionalWindow.SaveSignal.connect(self.tray_restart)

        self.WordWindow.DefaultSignal.connect(self.tray_restart)
        self.AdobeWindow.DefaultSignal.connect(self.tray_restart)
        self.ExcelWindow.DefaultSignal.connect(self.tray_restart)
        self.GenWindow.DefaultSignal.connect(self.tray_restart)   
        self.MiscWindow.DefaultSignal.connect(self.tray_restart)
        self.ConditionalWindow.DefaultSignal.connect(self.tray_restart)
        self.FileCallWindow.DefaultSignal.connect(self.tray_restart)
        self.ConditionalWindow.DefaultSignal.connect(self.tray_restart)

        self.PrefrencesWindow.SaveSignal.connect(self.tray_restart)
        



                                                                                                    

    
    def GeneralOptionsWindow(self):
        self.GenWindow.ShowGenModern()
 
 
    def AdobeOptionsWindow(self):    
        self.AdobeWindow.ShowAdobeModern()
   


    def ExcelOptionsWindow(self):  
        self.ExcelWindow.ShowExcelModern()
       


    def WordOptionsWindow(self):
        self.WordWindow.ShowWordModern()  


    def MiscOptionsWindow(self):
        self.MiscWindow.ShowMiscModern()  


    def FileCallsOptionsWindow(self): 
        self.FileCallWindow.ShowFileCallsModern()

    def OPEN_PREFRENCES(self):  
        self.PrefrencesWindow.ShowPreferncesModern()







    def OPEN_CONDITIONAL(self): 
        self.ConditionalWindow.ShowConditionalModern() 



    def change_state(self):
        importlib.reload(MainApp)
        if w.Toggle.isChecked() == 1:
            MainApp.StartHotkeys()
        else:
            MainApp.StopHotkeys()
            subprocess.run("TerminateAHK.bat", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


    def tray_start(self):
        if w.Toggle.isChecked() == 0:
            self.Toggle.setChecked(1)
        else:
            return

    def tray_stop(self):
        if w.Toggle.isChecked() == 1:
            self.Toggle.setChecked(0)
        else:
            return

    def tray_restart(self):
        if self.RestoreDefaults == 0:
            self.Toggle.setChecked(0)
            time.sleep(.5)
            self.Toggle.setChecked(1)
        else:
            return



    def Restore_All_Defaults(self):
        self.RestoreDefaults = 1
        dlg = CustomDialog(self)
        dlg.exec_()
        if self.SaveConfirmed == 1:
            self.GenWindow.SaveConfirmed = 1
            self.GenWindow.CallDefaultList()
            AdobeBackend.SaveConfirmed = 1
            self.AdobeWindow.CallDefaultList()
            ExcelBackend.SaveConfirmed = 1
            self.ExcelWindow.CallDefaultList()
            WordBackend.SaveConfirmed = 1
            self.WordWindow.CallDefaultList()
            MiscBackend.SaveConfirmed = 1
            self.MiscWindow.CallDefaultList()
            FileCallBackend.SaveConfirmed = 1
            self.FileCallWindow.CallDefaultList()
            self.Toggle.setChecked(0)
            time.sleep(.5)
            self.Toggle.setChecked(1)
            self.RestoreDefaults = 0
        else:
            self.RestoreDefaults = 0

    def ExportKeyboardLayout(self):
        global basedir
        caption = ""
        initial_dir = ""
        initial_filter = FILE_FILTERS[0]
        filters = ";;".join(FILE_FILTERS)
        filename, selected_filter = QFileDialog.getSaveFileName(
            self,
            caption=caption,
            directory=initial_dir,
            filter=filters,
            initialFilter=initial_filter,
        )
        if filename:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
            with open(f"{filename}", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ImportKeyboardLayout(self):
        caption = ""
        initial_dir = ""
        initial_filter = FILE_FILTERS[0]
        filters = ";;".join(FILE_FILTERS)


        filename, selected_filter = QFileDialog.getOpenFileName(
            self,
            caption=caption,
            directory=initial_dir,
            filter=filters,
            initialFilter=initial_filter,
        )

        if filename:
            a_file = open(f"{basedir}\JSON DEFAULT.json", "r")
            json_object = json.load(a_file)
            a_file.close() 
            temp = open(f"{filename}", "r")
            ImportFile = json.load(temp)
            diff = set(json_object.keys()) - set(ImportFile.keys()) 
            if len(diff):    
                raise Exception("INVALID JSON IMPORT")
            else:     
                with open(f"{filename}", "r") as f:
                    key = json.load(f)
                with open(f"{basedir}\JSON USER.json", "w") as f:
                    json.dump(key, f, indent=4, separators=(',', ': '))
                self.GenWindow.SetPlaceholderText()
                self.AdobeWindow.SetPlaceholderText()
                self.ExcelWindow.SetPlaceholderText()
                self.WordWindow.SetPlaceholderText()
                self.ConditionalWindow.SetPlaceholderText()
                self.FileCallWindow.SetPlaceholderText()
                self.tray_restart()
           
                


class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Save Changes?")

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("RESTORE ALL DEFAULTS?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def accept(self):
        Window.SaveConfirmed = 1
        self.close()

def TrayClicked(reason):
    global mw
    if reason == 3:
        mw.showNormal()

def QuitClicked():
    global tray
    global app
    tray.setVisible(False)
    w.Toggle.setChecked(0)
    app.quit()



w = Window()
    

# Create the tray
tray = QSystemTrayIcon()
menu = QMenu()
Quit = QAction("Quit")
Start = QAction("Start")
Stop = QAction("Stop")
Restart = QAction("Restart")
Quit.setFont(font)
Start.setFont(font)
Stop.setFont(font)
Restart.setFont(font)
Quit.triggered.connect(QuitClicked)
Start.triggered.connect(w.tray_start)
Stop.triggered.connect(w.tray_stop)
Restart.triggered.connect(w.tray_restart)
menu.addAction(Start)
menu.addAction(Stop)
menu.addAction(Quit)
menu.addAction(Restart)


w.Toggle.setChecked(1)


qtmodern.styles.dark(app)
mw = qtmodern.windows.ModernWindow(w)
tray.activated.connect(TrayClicked)
if w.PrefrencesWindow.MinStart.isChecked():
    mw.show()
tray.setContextMenu(menu)
tray.setVisible(True)
tray.setIcon(icon)
app.exec()
