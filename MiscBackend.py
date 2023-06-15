
import json
import os
from PyQt5.QtWidgets import QMainWindow, QLabel, QFrame, QDialog, QDialogButtonBox, QVBoxLayout, QShortcut
from MiscOptions import Ui_W4Window
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
        message = QLabel("RESTORE ALL VS_CODE DEFAULTS?")
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





class MiscOptionsBackend(QMainWindow, Ui_W4Window):
    SaveSignal = pyqtSignal(int)
    DefaultSignal = pyqtSignal(int)
    def __init__(self, *args, obj=None, **kwargs):
        super(MiscOptionsBackend, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("VS_CODE Hotkeys")
        self.SaveBtn_5.clicked.connect(self.CallFuncList)
        self.DefaultBtn_5.clicked.connect(self.CallDialog)
        self.SetPlaceholderText()
        self.P5_SEARCH.textChanged.connect(self.SearchText)
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
        


    def ShowMiscModern(self):
        global mw
        mw = qtmodern.windows.ModernWindow(self)
        mw.showMaximized()
        mw.activateWindow()    

    def SearchText(self):
        jtext = (self.P5_SEARCH.toPlainText()).lower()
        LabelList = [self.L11_5, self.L14_5, self.L45_5,
                     self.L70_5, self.L71_5, self.L87_5,]
        for x in LabelList:
            if jtext == "":
                x.setFrameShape(QFrame.NoFrame)
            else:
                if jtext in x.text().lower():
                    x.setFrameShape(QFrame.WinPanel)
                else:
                    x.setFrameShape(QFrame.NoFrame)

    def SelectFind(self):
        self.P5_SEARCH.setFocus()

    def CallFuncList(self):
        global a_file
        global json_object        
        FuncList = [self.UpdateKey_11, self.UpdateKey_14, self.UpdateKey_45,
                    self.UpdateKey_70, self.UpdateKey_71, self.UpdateKey_87,]

        PlainTextList = [self.P11_5, self.P14_5, self.P45_5,
                     self.P70_5, self.P71_5, self.P87_5]                  
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

        PlainTextList = [self.P11_5, self.P14_5, self.P45_5,
                    self.P70_5, self.P71_5, self.P87_5]

        DefaultList = [self.DefaultKey_11, self.DefaultKey_14, self.DefaultKey_45,
                        self.DefaultKey_70, self.DefaultKey_71, self.DefaultKey_87]
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
        self.P11_5.setPlaceholderText(f"{json_object['11.5 +MButton'][0]}")
        self.P14_5.setPlaceholderText(f"{json_object['14.5 ^MButton'][0]}")
        self.P45_5.setPlaceholderText(f"{json_object['45.5 Tab & MButton'][0]}")
        self.P70_5.setPlaceholderText(f"{json_object['70.5 CapsLock & Z'][0]}")
        self.P71_5.setPlaceholderText(f"{json_object['71.5 CapsLock & X'][0]}")
        self.P87_5.setPlaceholderText(f"{json_object['87.5 !LButton'][0]}")

    def UpdateKey_11(self, jtext):
        jtext = self.P11_5.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"11.5 +MButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_14(self, jtext):
        jtext = self.P14_5.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"14.5 ^MButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_45(self, jtext):
        jtext = self.P45_5.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"45.5 Tab & MButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))                

    def UpdateKey_70(self, jtext):
        jtext = self.P70_5.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"70.5 CapsLock & Z": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_71(self, jtext):
        jtext = self.P71_5.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"71.5 CapsLock & X": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        

    def UpdateKey_87(self, jtext):
        jtext = self.P87_5.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"87.5 !LButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))









    def DefaultKey_11(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['11.5 +MButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"11.5 +MButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_14(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['14.5 ^MButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"14.5 ^MButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_45(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['45.5 Tab & MButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"45.5 Tab & MButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))            

    def DefaultKey_70(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['70.5 CapsLock & Z'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"70.5 CapsLock & Z": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_71(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['71.5 CapsLock & X'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"71.5 CapsLock & X": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_87(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['87.5 !LButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"87.5 !LButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))
