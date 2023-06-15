
import json
import os
import re
from PyQt5.QtWidgets import QMainWindow, QLabel, QFrame, QDialog, QDialogButtonBox, QVBoxLayout, QShortcut
from FileCallsOptions import Ui_W4Window
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
        message = QLabel("CLEAR ALL FILE CALL KEYS?")
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





class FileCallsOptionsBackend(QMainWindow, Ui_W4Window):
    SaveSignal = pyqtSignal(int)
    DefaultSignal = pyqtSignal(int)
    def __init__(self, *args, obj=None, **kwargs):
        super(FileCallsOptionsBackend, self).__init__(*args, **kwargs)       
        self.setupUi(self)
        self.setWindowTitle("File Call Keys")
        self.SaveBtn_6.clicked.connect(self.CallFuncList)
        self.DefaultBtn_6.clicked.connect(self.CallDialog)
        self.SetPlaceholderText()
        self.P6_SEARCH.textChanged.connect(self.SearchText)
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
        
    def ShowFileCallsModern(self):
        global mw
        mw = qtmodern.windows.ModernWindow(self)
        mw.showMaximized()
        mw.activateWindow()

    def SearchText(self):
        jtext = (self.P6_SEARCH.toPlainText()).lower()
        LabelList = [self.L77_6, self.L78_6, self.L79_6, self.L80_6, self.L81_6, self.L82_6,
                     self.L83_6, self.L84_6, self.L94_6, self.L95_6]
        for x in LabelList:
            if jtext == "":
                x.setFrameShape(QFrame.NoFrame)
            else:
                if jtext in x.text().lower():
                    x.setFrameShape(QFrame.WinPanel)
                else:
                    x.setFrameShape(QFrame.NoFrame)

    def SelectFind(self):
        self.P6_SEARCH.setFocus()

    def CallFuncList(self):
        global a_file
        global json_object        
        FuncList = [self.UpdateKey_77, self.UpdateKey_78, self.UpdateKey_79, self.UpdateKey_80, self.UpdateKey_81, self.UpdateKey_82,
                    self.UpdateKey_83, self.UpdateKey_84, self.UpdateKey_94, self.UpdateKey_95]

        PlainTextList = [self.P77_6, self.P78_6, self.P79_6, self.P80_6, self.P81_6, self.P82_6,
                     self.P83_6, self.P84_6, self.P94_6, self.P95_6]                    

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
        DefaultList = [self.DefaultKey_77, self.DefaultKey_78, self.DefaultKey_79, self.DefaultKey_80, self.DefaultKey_81,
                        self.DefaultKey_82, self.DefaultKey_83, self.DefaultKey_84, self.DefaultKey_94, self.DefaultKey_95]

        PlainTextList = [self.P77_6, self.P78_6, self.P79_6, self.P80_6, self.P81_6, self.P82_6,
                    self.P83_6, self.P84_6, self.P94_6, self.P95_6]
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
        self.P77_6.setPlaceholderText(
            f"{json_object['77.6 CapsLock & F3'][0]}")
        self.P78_6.setPlaceholderText(
            f"{json_object['78.6 CapsLock & F4'][0]}")
        self.P79_6.setPlaceholderText(
            f"{json_object['79.6 CapsLock & F5'][0]}")
        self.P80_6.setPlaceholderText(
            f"{json_object['80.6 CapsLock & F6'][0]}")
        self.P81_6.setPlaceholderText(
            f"{json_object['81.6 CapsLock & F7'][0]}")
        self.P82_6.setPlaceholderText(
            f"{json_object['82.6 CapsLock & F8'][0]}")
        self.P83_6.setPlaceholderText(
            f"{json_object['83.6 CapsLock & F9'][0]}")
        self.P84_6.setPlaceholderText(
            f"{json_object['84.6 CapsLock & F10'][0]}")
        self.P94_6.setPlaceholderText(
            f"{json_object['94.6 CapsLock & F11'][0]}")
        self.P95_6.setPlaceholderText(
            f"{json_object['95.6 CapsLock & F12'][0]}")






    def UpdateKey_77(self, jtext):
        jtext = self.P77_6.toPlainText()
        if re.search("cls*",jtext):
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"77.6 CapsLock & F3": [""]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:            
            if jtext != "":
                with open(f"{basedir}\JSON USER.json", "r") as f:
                    key = json.load(f)
                    key.update({"77.6 CapsLock & F3": [jtext]})
                with open(f"{basedir}\JSON USER.json", "w") as f:
                    json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_78(self, jtext):
        jtext = self.P78_6.toPlainText()
        if re.search("cls*",jtext):
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"78.6 CapsLock & F4": [""]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:              
            if jtext != "":
                with open(f"{basedir}\JSON USER.json", "r") as f:
                    key = json.load(f)
                    key.update({"78.6 CapsLock & F4": [jtext]})
                with open(f"{basedir}\JSON USER.json", "w") as f:
                    json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_79(self, jtext):
        jtext = self.P79_6.toPlainText()
        if re.search("cls*",jtext):
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"79.6 CapsLock & F5": [""]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:              
            if jtext != "":
                with open(f"{basedir}\JSON USER.json", "r") as f:
                    key = json.load(f)
                    key.update({"79.6 CapsLock & F5": [jtext]})
                with open(f"{basedir}\JSON USER.json", "w") as f:
                    json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_80(self, jtext):
        jtext = self.P80_6.toPlainText()
        if re.search("cls*",jtext):
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"80.6 CapsLock & F6": [""]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:              
            if jtext != "":
                with open(f"{basedir}\JSON USER.json", "r") as f:
                    key = json.load(f)
                    key.update({"80.6 CapsLock & F6": [jtext]})
                with open(f"{basedir}\JSON USER.json", "w") as f:
                    json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_81(self, jtext):
        jtext = self.P81_6.toPlainText()
        if re.search("cls*",jtext):
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"81.6 CapsLock & F7": [""]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:              
            if jtext != "":
                with open(f"{basedir}\JSON USER.json", "r") as f:
                    key = json.load(f)
                    key.update({"81.6 CapsLock & F7": [jtext]})
                with open(f"{basedir}\JSON USER.json", "w") as f:
                    json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_82(self, jtext):
        jtext = self.P82_6.toPlainText()
        if re.search("cls*",jtext):
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"82.6 CapsLock & F8": [""]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:              
            if jtext != "":
                with open(f"{basedir}\JSON USER.json", "r") as f:
                    key = json.load(f)
                    key.update({"82.6 CapsLock & F8": [jtext]})
                with open(f"{basedir}\JSON USER.json", "w") as f:
                    json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_83(self, jtext):
        jtext = self.P83_6.toPlainText()
        if re.search("cls*",jtext):
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"83.6 CapsLock & F9": [""]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:              
            if jtext != "":
                with open(f"{basedir}\JSON USER.json", "r") as f:
                    key = json.load(f)
                    key.update({"83.6 CapsLock & F9": [jtext]})
                with open(f"{basedir}\JSON USER.json", "w") as f:
                    json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_84(self, jtext):
        jtext = self.P84_6.toPlainText()
        if re.search("cls*",jtext):
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"84.6 CapsLock & F10": [""]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:              
            if jtext != "":
                with open(f"{basedir}\JSON USER.json", "r") as f:
                    key = json.load(f)
                    key.update({"84.6 CapsLock & F10": [jtext]})
                with open(f"{basedir}\JSON USER.json", "w") as f:
                    json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_94(self, jtext):
        jtext = self.P94_6.toPlainText()
        if re.search("cls*",jtext):
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"94.6 CapsLock & F11": [""]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:              
            if jtext != "":
                with open(f"{basedir}\JSON USER.json", "r") as f:
                    key = json.load(f)
                    key.update({"94.6 CapsLock & F11": [jtext]})
                with open(f"{basedir}\JSON USER.json", "w") as f:
                    json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_95(self, jtext):
        jtext = self.P95_6.toPlainText()
        if re.search("cls*",jtext):
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"95.6 CapsLock & F12": [""]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:              
            if jtext != "":
                with open(f"{basedir}\JSON USER.json", "r") as f:
                    key = json.load(f)
                    key.update({"95.6 CapsLock & F12": [jtext]})
                with open(f"{basedir}\JSON USER.json", "w") as f:
                    json.dump(key, f, indent=4, separators=(',', ': '))









    def DefaultKey_77(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['77.6 CapsLock & F3'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"77.6 CapsLock & F3": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_78(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['78.6 CapsLock & F4'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"78.6 CapsLock & F4": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_79(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['79.6 CapsLock & F5'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"79.6 CapsLock & F5": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_80(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['80.6 CapsLock & F6'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"80.6 CapsLock & F6": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_81(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['81.6 CapsLock & F7'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"81.6 CapsLock & F7": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_82(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['82.6 CapsLock & F8'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"82.6 CapsLock & F8": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_83(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['83.6 CapsLock & F9'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"83.6 CapsLock & F9": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_84(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['84.6 CapsLock & F10'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"84.6 CapsLock & F10": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_94(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['94.6 CapsLock & F11'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"94.6 CapsLock & F11": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_95(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['95.6 CapsLock & F12'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"95.6 CapsLock & F12": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))
