
import json
import os
from PyQt5.QtWidgets import QMainWindow, QLabel, QFrame, QDialog, QDialogButtonBox, QVBoxLayout, QShortcut
from AdobeOptions import Ui_A2Window
from PyQt5 import QtGui
from PyQt5.QtGui import QKeySequence
import qtmodern.styles
import qtmodern.windows
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
        message = QLabel("RESTORE ALL ADOBE DEFAULTS?")
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








class AdobeOptionsBackend(QMainWindow, Ui_A2Window):
    SaveSignal = pyqtSignal(int)
    DefaultSignal = pyqtSignal(int)
    def __init__(self, *args, obj=None, **kwargs):
        super(AdobeOptionsBackend, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Adobe PDF Hotkeys")
        self.SetPlaceholderText()
        self.SaveBtn_2.clicked.connect(self.CallFuncList)
        self.DefaultBtn_2.clicked.connect(self.CallDialog)
        self.P2_SEARCH.textChanged.connect(self.SearchText)
        self.SaveShortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        self.SaveShortcut.activated.connect(self.CallFuncList)
        self.SearchShortcut = QShortcut(QKeySequence("Ctrl+F"), self)
        self.SearchShortcut.activated.connect(self.SelectFind)
        self.DefaultsShortcut = QShortcut(QKeySequence("Ctrl+D"), self)
        self.DefaultsShortcut.activated.connect(self.CallDialog)

    def CallDialog(self):
        dlg = CustomDialog()
        dlg.AcceptSignal.connect(self.CallDefaultList)
        dlg.exec_()

        

    def ShowAdobeModern(self):
        global mw
        mw = qtmodern.windows.ModernWindow(self)
        mw.showMaximized()
        mw.activateWindow()    

    def SearchText(self):
        jtext = (self.P2_SEARCH.toPlainText()).lower()
        LabelList = [self.L7_2, self.L8_2, self.L12_2, self.L13_2, self.L22_2, self.L23_2,
                     self.L43_2, self.L44_2, self.L45_2, self.L71_2, self.L88_2]
        for x in LabelList:
            if jtext == "":
                x.setFrameShape(QFrame.NoFrame)
            else:
                if jtext in x.text().lower():
                    x.setFrameShape(QFrame.WinPanel)
                else:
                    x.setFrameShape(QFrame.NoFrame)

    def SelectFind(self):
        self.P2_SEARCH.setFocus()

    def CallFuncList(self):
        global a_file
        global json_object        
        FuncList = [self.UpdateKey_7, self.UpdateKey_8, self.UpdateKey_12, self.UpdateKey_13, self.UpdateKey_22, self.UpdateKey_23,
                    self.UpdateKey_43, self.UpdateKey_44, self.UpdateKey_45, self.UpdateKey_71, self.UpdateKey_88]
                    
        PlainTextList = [self.P7_2, self.P8_2, self.P12_2, self.P13_2, self.P22_2, self.P23_2,
                        self.P43_2, self.P44_2, self.P45_2, self.P71_2, self.P88_2]
        for x in FuncList:
            x(self)            
        a_file = open(f"{basedir}\JSON USER.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        self.SetPlaceholderText()
        for x in PlainTextList:
            x.clear()
        self.SaveSignal.emit(1)            


    
    def CallDefaultList(self):
        global a_file
        global json_object
        global SaveConfirmed
        a_file = open(f"{basedir}\JSON USER.json", "r")
        json_object = json.load(a_file)
        a_file.close()           
        DefaultList = [self.DefaultKey_7, self.DefaultKey_8, self.DefaultKey_12, self.DefaultKey_13, self.DefaultKey_22, self.DefaultKey_23,
                        self.DefaultKey_43, self.DefaultKey_44, self.DefaultKey_45, self.DefaultKey_71, self.DefaultKey_88]
        PlainTextList = [self.P7_2, self.P8_2, self.P12_2, self.P13_2, self.P22_2, self.P23_2,
                    self.P43_2, self.P44_2, self.P45_2, self.P71_2, self.P88_2]
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
        self.P7_2.setPlaceholderText(f"{json_object['7.2 Tab & Z'][0]}")
        self.P8_2.setPlaceholderText(f"{json_object['8.2 Tab & X'][0]}")
        self.P12_2.setPlaceholderText(f"{json_object['12.2 +LButton'][0]}")
        self.P13_2.setPlaceholderText(f"{json_object['13.2 +RButton'][0]}")
        self.P22_2.setPlaceholderText(
            f"{json_object['22.2 CapsLock & RButton'][0]}")
        self.P23_2.setPlaceholderText(
            f"{json_object['23.2 CapsLock & LButton'][0]}")
        self.P43_2.setPlaceholderText(
            f"{json_object['43.2 Tab & RButton'][0]}")
        self.P44_2.setPlaceholderText(
            f"{json_object['44.2 Tab & LButton'][0]}")
        self.P45_2.setPlaceholderText(
            f"{json_object['45.2 Tab & MButton'][0]}")
        self.P71_2.setPlaceholderText(f"{json_object['71.2 CapsLock & X'][0]}")
        self.P88_2.setPlaceholderText(f"{json_object['88.2 ^Space'][0]}")





    def UpdateKey_7(self, jtext):
        jtext = self.P7_2.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"7.2 Tab & Z": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_8(self, jtext):
        jtext = self.P8_2.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"8.2 Tab & X": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_12(self, jtext):
        jtext = self.P12_2.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"12.2 +LButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_13(self, jtext):
        jtext = self.P13_2.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"13.2 +RButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_22(self, jtext):
        jtext = self.P22_2.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"22.2 CapsLock & RButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_23(self, jtext):
        jtext = self.P23_2.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"23.2 CapsLock & LButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_43(self, jtext):
        jtext = self.P43_2.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"43.2 Tab & RButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_44(self, jtext):
        jtext = self.P44_2.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"44.2 Tab & LButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_45(self, jtext):
        jtext = self.P45_2.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({'45.2 Tab & MButton': [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_71(self, jtext):
        jtext = self.P71_2.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"71.2 CapsLock & X": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_88(self, jtext):
        jtext = self.P88_2.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"88.2 ^Space": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))




    def DefaultKey_7(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['7.2 Tab & Z'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"7.2 Tab & Z": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_8(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['8.2 Tab & X'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"8.2 Tab & X": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_12(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['12.2 +LButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"12.2 +LButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_13(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['13.2 +RButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"13.2 +RButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_22(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['22.2 CapsLock & RButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"22.2 CapsLock & RButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_23(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['23.2 CapsLock & LButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"23.2 CapsLock & LButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_43(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['43.2 Tab & RButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"43.2 Tab & RButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_44(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['44.2 Tab & LButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"44.2 Tab & LButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_45(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['45.2 Tab & MButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({'45.2 Tab & MButton': [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_71(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['71.2 CapsLock & X'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"71.2 CapsLock & X": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_88(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['88.2 ^Space'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"88.2 ^Space": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))