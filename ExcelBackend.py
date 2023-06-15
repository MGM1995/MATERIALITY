
import json
import os
from PyQt5.QtWidgets import QMainWindow, QLabel, QFrame, QDialog, QDialogButtonBox, QVBoxLayout, QShortcut
from ExcelOptions import Ui_E3Window
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
        message = QLabel("RESTORE ALL EXCEL DEFAULTS?")
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




class ExcelOptionsBackend(QMainWindow, Ui_E3Window):
    SaveSignal = pyqtSignal(int)
    DefaultSignal = pyqtSignal(int)
    def __init__(self, *args, obj=None, **kwargs):
        super(ExcelOptionsBackend, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Excel Hotkeys")
        self.SetPlaceholderText()
        self.SaveBtn_3.clicked.connect(self.CallFuncList)
        self.DefaultBtn_3.clicked.connect(self.CallDialog)
        self.P3_SEARCH.textChanged.connect(self.SearchText)
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

    def ShowExcelModern(self):
        global mw
        mw = qtmodern.windows.ModernWindow(self)
        mw.showMaximized()
        mw.activateWindow()        


    def SearchText(self):
        jtext = (self.P3_SEARCH.toPlainText()).lower()
        LabelList = [self.L5_3, self.L6_3, self.L7_3, self.L8_3, self.L9_3,
                     self.L11_3, self.L14_3, self.L17_3, self.L21_3,
                     self.L24_3, self.L26_3, self.L27_3, self.L28_3,
                     self.L29_3, self.L30_3, self.L31_3, self.L32_3,
                     self.L35_3, self.L36_3, self.L40_3, self.L43_3,
                     self.L44_3, self.L45_3, self.L46_3, self.L57_3,
                     self.L63_3, self.L64_3, self.L65_3, self.L66_3,
                     self.L71_3, self.L85_3, self.L87_3,
                     self.L88_3]
        for x in LabelList:
            if jtext == "":
                x.setFrameShape(QFrame.NoFrame)
            else:
                if jtext in x.text().lower():
                    x.setFrameShape(QFrame.WinPanel)
                else:
                    x.setFrameShape(QFrame.NoFrame)

    def SelectFind(self):
        self.P3_SEARCH.setFocus()

    def CallFuncList(self):
        global a_file
        global json_object        
        FuncList = [self.UpdateKey_5, self.UpdateKey_6, self.UpdateKey_7, self.UpdateKey_8, self.UpdateKey_9,
                    self.UpdateKey_11, self.UpdateKey_14, self.UpdateKey_17, self.UpdateKey_21,
                    self.UpdateKey_24, self.UpdateKey_26, self.UpdateKey_27, self.UpdateKey_28,
                    self.UpdateKey_29, self.UpdateKey_30, self.UpdateKey_31, self.UpdateKey_32,
                    self.UpdateKey_35, self.UpdateKey_36, self.UpdateKey_40, self.UpdateKey_43,
                    self.UpdateKey_44, self.UpdateKey_45, self.UpdateKey_46, self.UpdateKey_57,
                    self.UpdateKey_63, self.UpdateKey_64, self.UpdateKey_65, self.UpdateKey_66,
                    self.UpdateKey_71, self.UpdateKey_85, self.UpdateKey_87,
                    self.UpdateKey_88]

        PlainTextList = [self.P5_3, self.P6_3, self.P7_3, self.P8_3, self.P9_3,
                    self.P11_3, self.P14_3, self.P17_3, self.P21_3,
                    self.P24_3, self.P26_3, self.P27_3, self.P28_3,
                    self.P29_3, self.P30_3, self.P31_3, self.P32_3,
                    self.P35_3, self.P36_3, self.P40_3, self.P43_3,
                    self.P44_3, self.P45_3, self.P46_3, self.P57_3,
                    self.P63_3, self.P64_3, self.P65_3, self.P66_3,
                    self.P71_3, self.P85_3, self.P87_3,
                    self.P88_3]               
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
        DefaultList = [self.DefaultKey_5, self.DefaultKey_6, self.DefaultKey_7, self.DefaultKey_8, self.DefaultKey_9,
                        self.DefaultKey_11, self.DefaultKey_14, self.DefaultKey_17, self.DefaultKey_21,
                        self.DefaultKey_24, self.DefaultKey_26, self.DefaultKey_27, self.DefaultKey_28,
                        self.DefaultKey_29, self.DefaultKey_30, self.DefaultKey_31, self.DefaultKey_32,
                        self.DefaultKey_35, self.DefaultKey_36, self.DefaultKey_40, self.DefaultKey_43,
                        self.DefaultKey_44, self.DefaultKey_45, self.DefaultKey_46, self.DefaultKey_57,
                        self.DefaultKey_63, self.DefaultKey_64, self.DefaultKey_65, self.DefaultKey_66,
                        self.DefaultKey_71, self.DefaultKey_85, self.DefaultKey_87,
                        self.DefaultKey_88]   
        PlainTextList = [self.P5_3, self.P6_3, self.P7_3, self.P8_3, self.P9_3,
                    self.P11_3, self.P14_3, self.P17_3, self.P21_3,
                    self.P24_3, self.P26_3, self.P27_3, self.P28_3,
                    self.P29_3, self.P30_3, self.P31_3, self.P32_3,
                    self.P35_3, self.P36_3, self.P40_3, self.P43_3,
                    self.P44_3, self.P45_3, self.P46_3, self.P57_3,
                    self.P63_3, self.P64_3, self.P65_3, self.P66_3,
                    self.P71_3, self.P85_3, self.P87_3,
                    self.P88_3]                             
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
        self.P5_3.setPlaceholderText(f"{json_object['5.3 Tab & WheelDown'][0]}")
        self.P6_3.setPlaceholderText(f"{json_object['6.3 Tab & WheelUp'][0]}")
        self.P7_3.setPlaceholderText(f"{json_object['7.3 Tab & Z'][0]}")
        self.P8_3.setPlaceholderText(f"{json_object['8.3 Tab & X'][0]}")
        self.P9_3.setPlaceholderText(f"{json_object['9.3 Tab & Space'][0]}")
        self.P11_3.setPlaceholderText(f"{json_object['11.3 +MButton'][0]}")
        self.P14_3.setPlaceholderText(f"{json_object['14.3 ^MButton'][0]}")
        self.P17_3.setPlaceholderText(f"{json_object['17.3 ^Q'][0]}")
        self.P21_3.setPlaceholderText(f"{json_object['21.3 ^+F'][0]}")
        self.P24_3.setPlaceholderText(f"{json_object['24.3 +Tab'][0]}")
        self.P26_3.setPlaceholderText(f"{json_object['26.3 CapsLock & Q'][0]}")
        self.P27_3.setPlaceholderText(f"{json_object['27.3 CapsLock & W'][0]}")
        self.P28_3.setPlaceholderText(f"{json_object['28.3 CapsLock & F'][0]}")
        self.P29_3.setPlaceholderText(f"{json_object['29.3 CapsLock & S'][0]}")
        self.P30_3.setPlaceholderText(f"{json_object['30.3 CapsLock & A'][0]}")
        self.P31_3.setPlaceholderText(f"{json_object['31.3 CapsLock & G'][0]}")
        self.P32_3.setPlaceholderText(f"{json_object['32.3 CapsLock & D'][0]}")
        self.P35_3.setPlaceholderText(f"{json_object['35.3 Tab & 2'][0]}")
        self.P36_3.setPlaceholderText(f"{json_object['36.32x Tab & S'][0]}")
        self.P40_3.setPlaceholderText(f"{json_object['40.3 Tab & 3'][0]}")
        self.P43_3.setPlaceholderText(
            f"{json_object['43.3 Tab & RButton'][0]}")
        self.P44_3.setPlaceholderText(
            f"{json_object['44.3 Tab & LButton'][0]}")
        self.P45_3.setPlaceholderText(
            f"{json_object['45.3 Tab & MButton'][0]}")
        self.P46_3.setPlaceholderText(f"{json_object['46.3 Tab & 1'][0]}")
        self.P57_3.setPlaceholderText(f"{json_object['57.3 !+MButton'][0]}")
        self.P63_3.setPlaceholderText(f"{json_object['63.3 Tab & 4'][0]}")
        self.P64_3.setPlaceholderText(f"{json_object['64.3 Tab & 5'][0]}")
        self.P65_3.setPlaceholderText(f"{json_object['65.3 Tab & 6'][0]}")
        self.P66_3.setPlaceholderText(f"{json_object['66.3 CapsLock & 1'][0]}")
        self.P71_3.setPlaceholderText(f"{json_object['71.3 CapsLock & X'][0]}")
        self.P85_3.setPlaceholderText(
            f"{json_object['85.3 CapsLock & Space'][0]}")
        self.P87_3.setPlaceholderText(f"{json_object['87.3 !LButton'][0]}")
        self.P88_3.setPlaceholderText(f"{json_object['88.3 ^Space'][0]}")




    def UpdateKey_5(self, jtext):
        jtext = self.P5_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"5.3 Tab & WheelDown": [jtext]})
            with open("JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_6(self, jtext):
        jtext = self.P6_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"6.3 Tab & WheelUp": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_7(self, jtext):
        jtext = self.P7_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"7.3 Tab & Z": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_8(self, jtext):
        jtext = self.P8_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"8.3 Tab & X": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_9(self, jtext):
        jtext = self.P9_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"9.3 Tab & Space": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_11(self, jtext):
        jtext = self.P11_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"11.3 +MButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_14(self, jtext):
        jtext = self.P14_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"14.3 ^MButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_17(self, jtext):
        jtext = self.P17_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"17.3 ^Q": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_21(self, jtext):
        jtext = self.P21_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"21.3 ^+F": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_24(self, jtext):
        jtext = self.P24_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"24.3 +Tab": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_26(self, jtext):
        jtext = self.P26_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"26.3 CapsLock & Q": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_27(self, jtext):
        jtext = self.P27_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"27.3 CapsLock & W": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_28(self, jtext):
        jtext = self.P28_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"28.3 CapsLock & F": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_29(self, jtext):
        jtext = self.P29_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"29.3 CapsLock & S": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_30(self, jtext):
        jtext = self.P30_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"30.3 CapsLock & A": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_31(self, jtext):
        jtext = self.P31_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"31.3 CapsLock & G": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_32(self, jtext):
        jtext = self.P32_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"32.3 CapsLock & D": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_35(self, jtext):
        jtext = self.P35_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"35.3 Tab & 2": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_36(self, jtext):
        jtext = self.P36_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"36.32x Tab & S": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_40(self, jtext):
        jtext = self.P40_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"40.3 Tab & 3": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_43(self, jtext):
        jtext = self.P43_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"43.3 Tab & RButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_44(self, jtext):
        jtext = self.P44_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"44.3 Tab & LButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_45(self, jtext):
        jtext = self.P45_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"45.3 Tab & MButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_46(self, jtext):
        jtext = self.P46_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"46.3 Tab & 1": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_57(self, jtext):
        jtext = self.P57_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"57.3 !+MButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_63(self, jtext):
        jtext = self.P63_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"63.3 Tab & 4": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_64(self, jtext):
        jtext = self.P64_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"64.3 Tab & 5": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_65(self, jtext):
        jtext = self.P65_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"65.3 Tab & 6": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_66(self, jtext):
        jtext = self.P66_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"66.3 CapsLock & 1": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_71(self, jtext):
        jtext = self.P71_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"71.3 CapsLock & X": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_85(self, jtext):
        jtext = self.P85_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"85.3 CapsLock & Space": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_87(self, jtext):
        jtext = self.P87_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"87.3 !LButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_88(self, jtext):
        jtext = self.P88_3.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"88.3 ^Space": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))




    def DefaultKey_5(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['5.3 Tab & WheelDown'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"5.3 Tab & WheelDown": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_6(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['6.3 Tab & WheelUp'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"6.3 Tab & WheelUp": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_7(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['7.3 Tab & Z'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"7.3 Tab & Z": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_8(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['8.3 Tab & X'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"8.3 Tab & X": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_9(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['9.3 Tab & Space'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"9.3 Tab & Space": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_11(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['11.3 +MButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"11.3 +MButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_14(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['14.3 ^MButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"14.3 ^MButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_17(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['17.3 ^Q'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"17.3 ^Q": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_21(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['21.3 ^+F'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"21.3 ^+F": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_24(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['24.3 +Tab'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"24.3 +Tab": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_26(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['26.3 CapsLock & Q'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"26.3 CapsLock & Q": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_27(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['27.3 CapsLock & W'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"27.3 CapsLock & W": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_28(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['28.3 CapsLock & F'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"28.3 CapsLock & F": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_29(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['29.3 CapsLock & S'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"29.3 CapsLock & S": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_30(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['30.3 CapsLock & A'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"30.3 CapsLock & A": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_31(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['31.3 CapsLock & G'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"31.3 CapsLock & G": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_32(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['32.3 CapsLock & D'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"32.3 CapsLock & D": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_35(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['35.3 Tab & 2'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"35.3 Tab & 2": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_36(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['36.32x Tab & S'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"36.32x Tab & S": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_40(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['40.3 Tab & 3'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"40.3 Tab & 3": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_43(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['43.3 Tab & RButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"43.3 Tab & RButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_44(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['44.3 Tab & LButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"44.3 Tab & LButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_45(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['45.3 Tab & MButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"45.3 Tab & MButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_46(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['46.3 Tab & 1'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"46.3 Tab & 1": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_57(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['57.3 !+MButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"57.3 !+MButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_63(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['63.3 Tab & 4'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"63.3 Tab & 4": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_64(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['64.3 Tab & 5'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"64.3 Tab & 5": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_65(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['65.3 Tab & 6'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"65.3 Tab & 6": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_66(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['66.3 CapsLock & 1'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"66.3 CapsLock & 1": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_71(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['71.3 CapsLock & X'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"71.3 CapsLock & X": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_85(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['85.3 CapsLock & Space'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"85.3 CapsLock & Space": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_87(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['87.3 !LButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"87.3 !LButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_88(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['88.3 ^Space'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"88.3 ^Space": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))
