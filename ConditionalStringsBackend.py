
import json
import os
from PyQt5.QtWidgets import QMainWindow, QLabel, QDialog, QDialogButtonBox, QVBoxLayout, QShortcut, QShortcut
from ConditionalStringsOptions import Ui_A2Window
from PyQt5.QtGui import QKeySequence
import qtmodern.styles
import qtmodern.windows
import subprocess
from PyQt5.QtCore import pyqtSignal


basedir = os.path.dirname(__file__)
mw = 1
SaveConfirmed = 0

a_file = open(f"{basedir}\JSON USER.json", "r")
json_object = json.load(a_file)
a_file.close()


class CustomDialog(QDialog):
    AcceptSignal = pyqtSignal(int)
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Save Changes?")

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("RESTORE ALL DEFAULT SCOPES?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def accept(self):
        global SaveConfirmed        
        SaveConfirmed = 1
        self.AcceptSignal.emit(1)
        self.hide()
      

    def reject(self):
        global SaveConfirmed  
        SaveConfirmed = 0
        self.hide()



class ConditionalStringsOptionsBackend(QMainWindow, Ui_A2Window):
    SaveSignal = pyqtSignal(int)
    DefaultSignal = pyqtSignal(int)
    def __init__(self, *args, obj=None, **kwargs):
        super(ConditionalStringsOptionsBackend, self).__init__(*args, **kwargs)        
        self.setupUi(self)
        self.setWindowTitle("Set Scope")
        self.SetPlaceholderText()
        self.SaveBtn_7.clicked.connect(self.CallFuncList)
        self.DefaultBtn_7.clicked.connect(self.CallDialog)
        self.SaveShortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        self.AHShortcut = QShortcut(QKeySequence("Ctrl+H"), self)
        self.AHShortcut.activated.connect(self.StartAH)
        self.SaveShortcut.activated.connect(self.CallFuncList)
        self.AHButton.clicked.connect(self.StartAH)
        self.DefaultsShortcut = QShortcut(QKeySequence("Ctrl+D"), self)
        self.DefaultsShortcut.activated.connect(self.CallDialog)

    def ShowConditionalModern(self):
        global mw
        mw = qtmodern.windows.ModernWindow(self)
        mw.showMaximized()
        mw.activateWindow()        

    def CallDialog(self):
        dlg = CustomDialog()
        dlg.AcceptSignal.connect(self.CallDefaultList)
        dlg.exec_()

    def CallFuncList(self):
        global a_file
        global json_object  
        PlainTextList =[self.PConditional_2,self.PConditional_3,self.PConditional_4,self.PConditional_5]      
        FuncList = [self.UpdateConditional_2, self.UpdateConditional_3,
                    self.UpdateConditional_4, self.UpdateConditional_5]

        for x in FuncList:
            x(self)            
        a_file = open(f"{basedir}\JSON USER.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        self.SetPlaceholderText()
        for x in PlainTextList:
            x.clear()
        self.SaveSignal.emit(1)            


    
    def StartAH(self):
        try:
            autohotkey_exe = f"{basedir}\\ahk\\AutoHotkey\\AutoHotkey.exe"
            script_file = f"{basedir}\\WindowSpy.ahk"
            subprocess.Popen([autohotkey_exe, script_file])
        except Exception:
            return



    def CallDefaultList(self):
        global a_file
        global json_object
        global SaveConfirmed
        a_file = open(f"{basedir}\JSON USER.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        PlainTextList =[self.PConditional_2,self.PConditional_3,self.PConditional_4,self.PConditional_5]
        DefaultList = [self.DefaultConditional_2, self.DefaultConditional_3,
                        self.DefaultConditional_4, self.DefaultConditional_5]
        for x in DefaultList:
            x()
        for x in PlainTextList:
            x.clear() 
        self.SetPlaceholderText()
        self.DefaultSignal.emit(1)           



    def SetPlaceholderText(self):
        global a_file
        global json_object
        a_file = open(f"{basedir}\JSON USER.json", "r")
        json_object = json.load(a_file)
        a_file.close()        
        self.PConditional_2.setPlaceholderText(
            f"{json_object['CONDITIONAL_2'][0]}")
        self.PConditional_3.setPlaceholderText(
            f"{json_object['CONDITIONAL_3'][0]}")
        self.PConditional_4.setPlaceholderText(
            f"{json_object['CONDITIONAL_4'][0]}")
        self.PConditional_5.setPlaceholderText(
            f"{json_object['CONDITIONAL_5'][0]}")






    def UpdateConditional_2(self, jtext):
        jtext = self.PConditional_2.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"CONDITIONAL_2": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateConditional_3(self, jtext):
        jtext = self.PConditional_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"CONDITIONAL_3": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateConditional_4(self, jtext):
        jtext = self.PConditional_4.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"CONDITIONAL_4": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateConditional_5(self, jtext):
        jtext = self.PConditional_5.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"CONDITIONAL_5": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))







    def DefaultConditional_2(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['CONDITIONAL_2'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"CONDITIONAL_2": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultConditional_3(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['CONDITIONAL_3'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"CONDITIONAL_3": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultConditional_4(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['CONDITIONAL_4'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"CONDITIONAL_4": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultConditional_5(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['CONDITIONAL_5'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"CONDITIONAL_5": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))
