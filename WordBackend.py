
import json
import os
from PyQt5.QtWidgets import QMainWindow, QLabel, QFrame, QDialog, QDialogButtonBox, QVBoxLayout, QShortcut
from WordOptions import Ui_W4Window
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
    def __init__(self, parent=None):
        super().__init__(parent)


        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.setWindowTitle("Save Changes?")

        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("RESTORE ALL WORD DEFAULTS?")
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





class WordOptionsBackend(QMainWindow, Ui_W4Window):
    SaveSignal = pyqtSignal(int)
    DefaultSignal = pyqtSignal(int) 
    def __init__(self, *args, obj=None, **kwargs):
        super(WordOptionsBackend, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Word Hotkeys")
        self.SaveBtn_4.clicked.connect(self.CallFuncList)
        self.DefaultBtn_4.clicked.connect(self.CallDialog)
        self.SetPlaceholderText()
        self.P4_SEARCH.textChanged.connect(self.SearchText)
        self.SearchShortcut = QShortcut(QKeySequence("Ctrl+F"), self)
        self.SaveShortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        self.SearchShortcut.activated.connect(self.SelectFind)
        self.SaveShortcut.activated.connect(self.CallFuncList)
        self.DefaultsShortcut = QShortcut(QKeySequence("Ctrl+D"), self)
        self.DefaultsShortcut.activated.connect(self.CallDialog)
        


    def CallDialog(self):
        dlg = CustomDialog()
        dlg.AcceptSignal.connect(self.CallDefaultList)
        dlg.exec_()



    def ShowWordModern(self):
        global mw
        mw = qtmodern.windows.ModernWindow(self)
        mw.showMaximized()
        mw.activateWindow()

    def CallFuncList(self):
        global a_file
        global json_object
        PlainTextList = [self.P5_4, self.P6_4, self.P7_4, self.P8_4, self.P16_4, self.P24_4,
                self.P33_4, self.P41_4, self.P60_4, self.P61_4, self.P62_4,
                self.P71_4, self.P75_4]
        FuncList = [self.UpdateKey_5, self.UpdateKey_6, self.UpdateKey_7, self.UpdateKey_8, self.UpdateKey_16, self.UpdateKey_24,
                    self.UpdateKey_33, self.UpdateKey_41, self.UpdateKey_60, self.UpdateKey_61, self.UpdateKey_62,
                    self.UpdateKey_71, self.UpdateKey_75]

        for x in FuncList:
            x(self)            
        a_file = open(f"{basedir}\JSON USER.json", "r")
        json_object = json.load(a_file)
        a_file.close()
        self.SetPlaceholderText()
        for x in PlainTextList:
            x.clear()
        self.SaveSignal.emit(1)

    def SearchText(self):
        jtext = (self.P4_SEARCH.toPlainText()).lower()
        LabelList = [self.L5_4, self.L6_4, self.L7_4, self.L8_4, self.L16_4, self.L24_4,
                     self.L33_4, self.L41_4, self.L60_4, self.L61_4, self.L62_4,
                     self.L71_4, self.L75_4]
        for x in LabelList:
            if jtext == "":
                x.setFrameShape(QFrame.NoFrame)
            else:
                if jtext in x.text().lower():
                    x.setFrameShape(QFrame.WinPanel)
                else:
                    x.setFrameShape(QFrame.NoFrame)

    def SelectFind(self):
        self.P4_SEARCH.setFocus()







    def CallDefaultList(self):
        global a_file
        global json_object
        global SaveConfirmed
        a_file = open(f"{basedir}\JSON USER.json", "r")
        json_object = json.load(a_file)
        a_file.close()

        PlainTextList = [self.P5_4, self.P6_4, self.P7_4, self.P8_4, self.P16_4, self.P24_4,
                    self.P33_4, self.P41_4, self.P60_4, self.P61_4, self.P62_4,
                    self.P71_4, self.P75_4] 

        DefaultList = [self.DefaultKey_5, self.DefaultKey_6, self.DefaultKey_7, self.DefaultKey_8, self.DefaultKey_16, self.DefaultKey_24,
                        self.DefaultKey_33, self.DefaultKey_41, self.DefaultKey_60, self.DefaultKey_61, self.DefaultKey_62,
                        self.DefaultKey_71, self.DefaultKey_75]  
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
        self.P5_4.setPlaceholderText(
            f"{json_object['5.4 Tab & WheelDown'][0]}")
        self.P6_4.setPlaceholderText(f"{json_object['6.4 Tab & WheelUp'][0]}")
        self.P7_4.setPlaceholderText(f"{json_object['7.4 Tab & Z'][0]}")
        self.P8_4.setPlaceholderText(f"{json_object['8.4 Tab & X'][0]}")
        self.P16_4.setPlaceholderText(f"{json_object['16.4 +Capslock'][0]}")
        self.P24_4.setPlaceholderText(f"{json_object['24.4 +Tab'][0]}")
        self.P33_4.setPlaceholderText(f"{json_object['33.4 CapsLock & `'][0]}")
        self.P41_4.setPlaceholderText(f"{json_object['41.4 +`'][0]}")
        self.P60_4.setPlaceholderText(f"{json_object['60.4 ^W'][0]}")
        self.P61_4.setPlaceholderText(f"{json_object['61.4 Tab & R'][0]}")
        self.P62_4.setPlaceholderText(f"{json_object['62.4 Tab & T'][0]}")
        self.P71_4.setPlaceholderText(f"{json_object['71.4 CapsLock & X'][0]}")
        self.P75_4.setPlaceholderText(
            f"{json_object['75.4 CapsLock & F1'][0]}")

    def UpdateKey_5(self, jtext):
        jtext = self.P5_4.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"5.4 Tab & WheelDown": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_6(self, jtext):
        jtext = self.P6_4.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"6.4 Tab & WheelUp": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_7(self, jtext):
        jtext = self.P7_4.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"7.4 Tab & Z": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_8(self, jtext):
        jtext = self.P8_4.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"8.4 Tab & X": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_16(self, jtext):
        jtext = self.P16_4.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"16.4 +Capslock": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_24(self, jtext):
        jtext = self.P24_4.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"24.4 +Tab": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_33(self, jtext):
        jtext = self.P33_4.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"33.4 CapsLock & `": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_41(self, jtext):
        jtext = self.P41_4.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"41.4 +`": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_60(self, jtext):
        jtext = self.P60_4.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"60.4 ^W": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_61(self, jtext):
        jtext = self.P61_4.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"61.4 Tab & R": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_62(self, jtext):
        jtext = self.P62_4.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"62.4 Tab & T": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_71(self, jtext):
        jtext = self.P71_4.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"71.4 CapsLock & X": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_75(self, jtext):
        jtext = self.P75_4.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"75.4 CapsLock & F1": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))







    def DefaultKey_5(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['5.4 Tab & WheelDown'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"5.4 Tab & WheelDown": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_6(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['6.4 Tab & WheelUp'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"6.4 Tab & WheelUp": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_7(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['7.4 Tab & Z'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"7.4 Tab & Z": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_8(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['8.4 Tab & X'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"8.4 Tab & X": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_16(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['16.4 +Capslock'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"16.4 +Capslock": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_24(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['24.4 +Tab'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"24.4 +Tab": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_33(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['33.4 CapsLock & `'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"33.4 CapsLock & `": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_41(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['41.4 +`'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"41.4 +`": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_60(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['60.4 ^W'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"60.4 ^W": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_61(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['61.4 Tab & R'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"61.4 Tab & R": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_62(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['62.4 Tab & T'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"62.4 Tab & T": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_71(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['71.4 CapsLock & X'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"71.4 CapsLock & X": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_75(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['75.4 CapsLock & F1'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"75.4 CapsLock & F1": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))
