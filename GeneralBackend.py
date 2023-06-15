
import json
import os
from PyQt5.QtWidgets import QMainWindow, QLabel, QFrame, QDialog, QDialogButtonBox, QVBoxLayout, QShortcut
from GeneralOptions import Ui_G1Window
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
        message = QLabel("RESTORE ALL GENERAL DEFAULTS?")
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



class GeneralOptionsBackend(QMainWindow, Ui_G1Window):
    SaveSignal = pyqtSignal(int)
    DefaultSignal = pyqtSignal(int)
    def __init__(self,*args, obj=None, **kwargs):
        super(GeneralOptionsBackend, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("General Hotkeys")
        self.SetPlaceholderText()
        self.SaveBtn_1.clicked.connect(self.CallFuncList)
        self.DefaultBtn_1.clicked.connect(self.CallDialog)
        self.P1_SEARCH.textChanged.connect(self.SearchText)
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

    def ShowGenModern(self):
        global mw
        mw = qtmodern.windows.ModernWindow(self)
        mw.showMaximized()
        mw.activateWindow()


    def SearchText(self):
        jtext = (self.P1_SEARCH.toPlainText()).lower()
        LabelList = [self.L1_1, self.L2_1, self.L3_1, self.L4_1, self.L7_1, self.L10_1,
                     self.L11_1, self.L12_1, self.L13_1, self.L14_1, self.L15_1, self.L16_1, self.L17_1, self.L18_1,
                     self.L19_1, self.L20_1, self.L22_1, self.L23_1, self.L24_1, self.L25_1, self.L33_1,
                     self.L34_1, self.L36_1, self.L37_1, self.L38_1, self.L39_1, self.L41_1, self.L42_1,
                     self.L47_1, self.L48_1, self.L49_1, self.L50_1, self.L51_1, self.L52_1, self.L53_1, self.L54_1,
                     self.L55_1, self.L56_1, self.L58_1, self.L59_1, self.L64_1, self.L65_1, self.L67_1,
                     self.L68_1, self.L69_1, self.L70_1, self.L72_1, self.L73_1, self.L74_1, self.L76_1,
                     self.L86_1, self.L87_1, self.L88_1, self.L89_1, self.L90_1, self.L91_1,
                     self.L92_1, self.L93_1, self.L93_12x, self.L96_1, self.L97_1]
        for x in LabelList:
            if jtext == "":
                x.setFrameShape(QFrame.NoFrame)
            else:
                if jtext in x.text().lower():
                    x.setFrameShape(QFrame.WinPanel)
                else:
                    x.setFrameShape(QFrame.NoFrame)

    def SelectFind(self):
        self.P1_SEARCH.setFocus()

    def CallFuncList(self):
        global a_file
        global json_object        
        FuncList = [self.UpdateKey_1, self.UpdateKey_2, self.UpdateKey_3, self.UpdateKey_4, self.UpdateKey_7, self.UpdateKey_10,
                    self.UpdateKey_11, self.UpdateKey_12, self.UpdateKey_13, self.UpdateKey_14, self.UpdateKey_15, self.UpdateKey_16, self.UpdateKey_17, self.UpdateKey_18,
                    self.UpdateKey_19, self.UpdateKey_20, self.UpdateKey_22, self.UpdateKey_23, self.UpdateKey_24, self.UpdateKey_25, self.UpdateKey_33,
                    self.UpdateKey_34, self.UpdateKey_36, self.UpdateKey_37, self.UpdateKey_38, self.UpdateKey_39, self.UpdateKey_41, self.UpdateKey_42,
                    self.UpdateKey_47, self.UpdateKey_48, self.UpdateKey_49, self.UpdateKey_50, self.UpdateKey_51, self.UpdateKey_52, self.UpdateKey_53, self.UpdateKey_54,
                    self.UpdateKey_55, self.UpdateKey_56, self.UpdateKey_58, self.UpdateKey_59, self.UpdateKey_64, self.UpdateKey_65, self.UpdateKey_67,
                    self.UpdateKey_68, self.UpdateKey_69, self.UpdateKey_70, self.UpdateKey_72, self.UpdateKey_73, self.UpdateKey_74, self.UpdateKey_76,
                    self.UpdateKey_86, self.UpdateKey_87, self.UpdateKey_88, self.UpdateKey_89, self.UpdateKey_90, self.UpdateKey_91,
                    self.UpdateKey_92, self.UpdateKey_93, self.UpdateKey_93_12x, self.UpdateKey_96, self.UpdateKey_97]

        PlainTextList = [self.P1_1, self.P2_1, self.P3_1, self.P4_1, self.P7_1, self.P10_1,
                    self.P11_1, self.P12_1, self.P13_1, self.P14_1, self.P15_1, self.P16_1, self.P17_1, self.P18_1,
                    self.P19_1, self.P20_1, self.P22_1, self.P23_1, self.P24_1, self.P25_1, self.P33_1,
                    self.P34_1, self.P36_1, self.P37_1, self.P38_1, self.P39_1, self.P41_1, self.P42_1,
                    self.P47_1, self.P48_1, self.P49_1, self.P50_1, self.P51_1, self.P52_1, self.P53_1, self.P54_1,
                    self.P55_1, self.P56_1, self.P58_1, self.P59_1, self.P64_1, self.P65_1, self.P67_1,
                    self.P68_1, self.P69_1, self.P70_1, self.P72_1, self.P73_1, self.P74_1, self.P76_1,
                    self.P86_1, self.P87_1, self.P88_1, self.P89_1, self.P90_1, self.P91_1,
                    self.P92_1, self.P93_1, self.P93_12x, self.P96_1, self.P97_1]   
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
        DefaultList = [self.DefaultKey_1, self.DefaultKey_2, self.DefaultKey_3, self.DefaultKey_4, self.DefaultKey_7, self.DefaultKey_10,
                        self.DefaultKey_11, self.DefaultKey_12, self.DefaultKey_13, self.DefaultKey_14, self.DefaultKey_15, self.DefaultKey_16, self.DefaultKey_17, self.DefaultKey_18,
                        self.DefaultKey_19, self.DefaultKey_20, self.DefaultKey_22, self.DefaultKey_23, self.DefaultKey_24, self.DefaultKey_25, self.DefaultKey_33,
                        self.DefaultKey_34, self.DefaultKey_36, self.DefaultKey_37, self.DefaultKey_38, self.DefaultKey_39, self.DefaultKey_41, self.DefaultKey_42,
                        self.DefaultKey_47, self.DefaultKey_48, self.DefaultKey_49, self.DefaultKey_50, self.DefaultKey_51, self.DefaultKey_52, self.DefaultKey_53, self.DefaultKey_54,
                        self.DefaultKey_55, self.DefaultKey_56, self.DefaultKey_58, self.DefaultKey_59, self.DefaultKey_64, self.DefaultKey_65, self.DefaultKey_67,
                        self.DefaultKey_68, self.DefaultKey_69, self.DefaultKey_70, self.DefaultKey_72, self.DefaultKey_73, self.DefaultKey_74, self.DefaultKey_76,
                        self.DefaultKey_86, self.DefaultKey_87, self.DefaultKey_88, self.DefaultKey_89, self.DefaultKey_90, self.DefaultKey_91,
                        self.DefaultKey_92, self.DefaultKey_93, self.DefaultKey_93_12x, self.DefaultKey_96, self.DefaultKey_97]

        PlainTextList = [self.P1_1, self.P2_1, self.P3_1, self.P4_1, self.P7_1, self.P10_1,
                    self.P11_1, self.P12_1, self.P13_1, self.P14_1, self.P15_1, self.P16_1, self.P17_1, self.P18_1,
                    self.P19_1, self.P20_1, self.P22_1, self.P23_1, self.P24_1, self.P25_1, self.P33_1,
                    self.P34_1, self.P36_1, self.P37_1, self.P38_1, self.P39_1, self.P41_1, self.P42_1,
                    self.P47_1, self.P48_1, self.P49_1, self.P50_1, self.P51_1, self.P52_1, self.P53_1, self.P54_1,
                    self.P55_1, self.P56_1, self.P58_1, self.P59_1, self.P64_1, self.P65_1, self.P67_1,
                    self.P68_1, self.P69_1, self.P70_1, self.P72_1, self.P73_1, self.P74_1, self.P76_1,
                    self.P86_1, self.P87_1, self.P88_1, self.P89_1, self.P90_1, self.P91_1,
                    self.P92_1, self.P93_1, self.P93_12x, self.P96_1, self.P97_1]                                              
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
        self.P1_1.setPlaceholderText(f"{json_object['1.1 +WheelDown'][0]}")
        self.P2_1.setPlaceholderText(f"{json_object['2.1 +WheelUp'][0]}")
        self.P3_1.setPlaceholderText(f"{json_object['3.1 #CapsLock'][0]}")
        self.P4_1.setPlaceholderText(f"{json_object['4.1 !`'][0]}")
        self.P7_1.setPlaceholderText(f"{json_object['7.1 Tab & Z'][0]}")
        self.P10_1.setPlaceholderText(f"{json_object['10.1 MButton'][0]}")
        self.P11_1.setPlaceholderText(f"{json_object['11.1 +MButton'][0]}")
        self.P12_1.setPlaceholderText(f"{json_object['12.1 +LButton'][0]}")
        self.P13_1.setPlaceholderText(f"{json_object['13.1 +RButton'][0]}")
        self.P14_1.setPlaceholderText(f"{json_object['14.1 ^MButton'][0]}")
        if (f"{json_object['15.1 CapsLock & 5'][0]}") == "":
            self.P15_1.setPlaceholderText("FREE KEY")
        else:
            self.P15_1.setPlaceholderText(
                f"{json_object['15.1 CapsLock & 5'][0]}")
        self.P16_1.setPlaceholderText(f"{json_object['16.1 +Capslock'][0]}")
        self.P17_1.setPlaceholderText(f"{json_object['17.1 ^Q'][0]}")
        self.P18_1.setPlaceholderText(f"{json_object['18.1 ^!LButton'][0]}")
        self.P19_1.setPlaceholderText(f"{json_object['19.1 ^!RButton'][0]}")
        self.P20_1.setPlaceholderText(f"{json_object['20.1 ^+Q'][0]}")
        self.P22_1.setPlaceholderText(
            f"{json_object['22.1 CapsLock & RButton'][0]}")
        self.P23_1.setPlaceholderText(
            f"{json_object['23.1 CapsLock & LButton'][0]}")
        self.P24_1.setPlaceholderText(f"{json_object['24.1 +Tab'][0]}")
        self.P25_1.setPlaceholderText(
            f"{json_object['25.1 CapsLock & MButton'][0]}")
        self.P33_1.setPlaceholderText(f"{json_object['33.1 CapsLock & `'][0]}")
        self.P34_1.setPlaceholderText(f"{json_object['34.12x CapsLock'][0]}")
        self.P36_1.setPlaceholderText(f"{json_object['36.1 Tab & S'][0]}")
        self.P37_1.setPlaceholderText(f"{json_object['37.1 Tab & W'][0]}")
        self.P38_1.setPlaceholderText(f"{json_object['38.1 Tab & A'][0]}")
        self.P39_1.setPlaceholderText(f"{json_object['39.1 Tab & D'][0]}")
        self.P41_1.setPlaceholderText(f"{json_object['41.1 +`'][0]}")
        self.P42_1.setPlaceholderText(f"{json_object['42.1 Tab & Q'][0]}")
        self.P47_1.setPlaceholderText(f"{json_object['47.1 Tab & F1'][0]}")
        if (f"{json_object['48.1 Tab & F2'][0]}") == "":
            self.P48_1.setPlaceholderText("FREE KEY")
        else:
            self.P48_1.setPlaceholderText(f"{json_object['48.1 Tab & F2'][0]}")
        if (f"{json_object['49.1 Tab & F3'][0]}") == "":
            self.P49_1.setPlaceholderText("FREE KEY")
        else:
            self.P49_1.setPlaceholderText(f"{json_object['49.1 Tab & F3'][0]}")
        if (f"{json_object['50.1 Tab & F4'][0]}") == "":
            self.P50_1.setPlaceholderText("FREE KEY")
        else:
            self.P50_1.setPlaceholderText(f"{json_object['50.1 Tab & F4'][0]}")
        if (f"{json_object['51.1 CapsLock & 6'][0]}") == "":
            self.P51_1.setPlaceholderText("FREE KEY")
        else:
            self.P51_1.setPlaceholderText(
                f"{json_object['51.1 CapsLock & 6'][0]}")
        self.P52_1.setPlaceholderText(f"{json_object['52.12x Alt'][0]}")
        self.P53_1.setPlaceholderText(f"{json_object['53.1 !MButton'][0]}")
        if (f"{json_object['54.1 !CapsLock'][0]}") == "":
            self.P54_1.setPlaceholderText("FREE KEY")
        else:
            self.P54_1.setPlaceholderText(
                f"{json_object['54.1 !CapsLock'][0]}")
        self.P55_1.setPlaceholderText(f"{json_object['55.1 !+LButton'][0]}")
        self.P56_1.setPlaceholderText(f"{json_object['56.1 !+RButton'][0]}")
        self.P58_1.setPlaceholderText(f"{json_object['58.1 `'][0]}")
        self.P59_1.setPlaceholderText(f"{json_object['59.1 ^+!MButton'][0]}")
        self.P64_1.setPlaceholderText(f"{json_object['64.1 Tab & 5'][0]}")
        self.P65_1.setPlaceholderText(f"{json_object['65.1 Tab & 6'][0]}")
        if (f"{json_object['67.1 CapsLock & 2'][0]}") == "":
            self.P67_1.setPlaceholderText("FREE KEY")
        else:
            self.P67_1.setPlaceholderText(
                f"{json_object['67.1 CapsLock & 2'][0]}")
        self.P68_1.setPlaceholderText(f"{json_object['68.1 CapsLock & 3'][0]}")
        self.P69_1.setPlaceholderText(f"{json_object['69.1 CapsLock & 4'][0]}")
        self.P70_1.setPlaceholderText(f"{json_object['70.1 CapsLock & Z'][0]}")
        self.P72_1.setPlaceholderText(f"{json_object['72.1 ^+Space'][0]}")
        self.P73_1.setPlaceholderText(f"{json_object['73.1 CapsLock & R'][0]}")
        self.P74_1.setPlaceholderText(f"{json_object['74.1 CapsLock & E'][0]}")
        self.P76_1.setPlaceholderText(
            f"{json_object['76.1 CapsLock & F2'][0]}")
        self.P86_1.setPlaceholderText(f"{json_object['86.1 ^+MButton'][0]}")
        self.P87_1.setPlaceholderText(f"{json_object['87.1 !LButton'][0]}")
        self.P88_1.setPlaceholderText(f"{json_object['88.1 ^Space'][0]}")
        self.P89_1.setPlaceholderText(
            f"{json_object['89.1 ~Alt & ~Tab Up'][0]}")
        self.P90_1.setPlaceholderText(f"{json_object['90.1 Tab Tilde'][0]}")
        self.P91_1.setPlaceholderText(f"{json_object['91.1 ^x'][0]}")
        self.P92_1.setPlaceholderText(f"{json_object['92.1 ^+X'][0]}")
        self.P93_1.setPlaceholderText(f"{json_object['93.1 ^!MButton'][0]}")
        self.P93_12x.setPlaceholderText(
            f"{json_object['93.12x ^!MButton'][0]}")
        if (f"{json_object['96.1 Tab & F5'][0]}") == "":
            self.P96_1.setPlaceholderText("FREE KEY")
        else:
            self.P96_1.setPlaceholderText(f"{json_object['96.1 Tab & F5'][0]}")
        if (f"{json_object['97.1 Tab & F6'][0]}") == "":
            self.P97_1.setPlaceholderText("FREE KEY")
        else:
            self.P97_1.setPlaceholderText(f"{json_object['97.1 Tab & F6'][0]}")

    def UpdateKey_1(self, jtext):
        jtext = self.P1_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"1.1 +WheelDown": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_2(self, jtext):
        jtext = self.P2_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"2.1 +WheelUp": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_3(self, jtext):
        jtext = self.P3_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"3.1 #CapsLock": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_4(self, jtext):
        jtext = self.P4_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"4.1 !`": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_7(self, jtext):
        jtext = self.P7_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"7.1 Tab & Z": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_10(self, jtext):
        jtext = self.P10_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"10.1 MButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_11(self, jtext):
        jtext = self.P11_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"11.1 +MButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_12(self, jtext):
        jtext = self.P12_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"12.1 +LButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_13(self, jtext):
        jtext = self.P13_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"13.1 +RButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_14(self, jtext):
        jtext = self.P14_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"14.1 ^MButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_15(self, jtext):
        jtext = self.P15_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"15.1 CapsLock & 5": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_16(self, jtext):
        jtext = self.P16_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"16.1 +Capslock": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_17(self, jtext):
        jtext = self.P17_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"17.1 ^Q": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_18(self, jtext):
        jtext = self.P18_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"18.1 ^!LButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_19(self, jtext):
        jtext = self.P19_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"19.1 ^!RButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_20(self, jtext):
        jtext = self.P20_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"20.1 ^+Q": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_22(self, jtext):
        jtext = self.P22_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"22.1 CapsLock & RButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_23(self, jtext):
        jtext = self.P23_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"23.1 CapsLock & LButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_24(self, jtext):
        jtext = self.P24_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"24.1 +Tab": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_25(self, jtext):
        jtext = self.P25_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"25.1 CapsLock & MButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_33(self, jtext):
        jtext = self.P33_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"33.1 CapsLock & `": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_34(self, jtext):
        jtext = self.P34_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"34.12x CapsLock": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_36(self, jtext):
        jtext = self.P36_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"36.1 Tab & S": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_37(self, jtext):
        jtext = self.P37_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"37.1 Tab & W": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_38(self, jtext):
        jtext = self.P38_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"38.1 Tab & A": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_39(self, jtext):
        jtext = self.P39_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"39.1 Tab & D": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_41(self, jtext):
        jtext = self.P41_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"41.1 +`": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_42(self, jtext):
        jtext = self.P42_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"42.1 Tab & Q": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_47(self, jtext):
        jtext = self.P47_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"47.1 Tab & F1": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_48(self, jtext):
        jtext = self.P48_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"48.1 Tab & F2": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_49(self, jtext):
        jtext = self.P49_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"49.1 Tab & F3": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_50(self, jtext):
        jtext = self.P50_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"50.1 Tab & F4": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_51(self, jtext):
        jtext = self.P51_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"51.1 CapsLock & 6": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_52(self, jtext):
        jtext = self.P52_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"52.12x Alt": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_53(self, jtext):
        jtext = self.P53_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"53.1 !MButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_54(self, jtext):
        jtext = self.P54_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"54.1 !CapsLock": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_55(self, jtext):
        jtext = self.P55_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"55.1 !+LButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_56(self, jtext):
        jtext = self.P56_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"56.1 !+RButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))


    def UpdateKey_58(self, jtext):
        jtext = self.P58_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"58.1 `": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_59(self, jtext):
        jtext = self.P59_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"59.1 ^+!MButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_64(self, jtext):
        jtext = self.P64_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"64.1 Tab & 5": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_65(self, jtext):
        jtext = self.P65_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"65.1 Tab & 6": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_67(self, jtext):
        jtext = self.P67_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"67.1 CapsLock & 2": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_68(self, jtext):
        jtext = self.P68_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"68.1 CapsLock & 3": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_69(self, jtext):
        jtext = self.P69_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"69.1 CapsLock & 4": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_70(self, jtext):
        jtext = self.P70_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"70.1 CapsLock & Z": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_72(self, jtext):
        jtext = self.P72_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"72.1 ^+Space": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_73(self, jtext):
        jtext = self.P73_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"73.1 CapsLock & R": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_74(self, jtext):
        jtext = self.P74_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"74.1 CapsLock & E": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_76(self, jtext):
        jtext = self.P76_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"76.1 CapsLock & F2": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_86(self, jtext):
        jtext = self.P86_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"86.1 ^+MButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_87(self, jtext):
        jtext = self.P87_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"87.1 !LButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_88(self, jtext):
        jtext = self.P88_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"88.1 ^Space": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_89(self, jtext):
        jtext = self.P89_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"89.1 ~Alt & ~Tab Up": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_90(self, jtext):
        jtext = self.P90_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"90.1 Tab Tilde": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_91(self, jtext):
        jtext = self.P91_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"91.1 ^x": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_92(self, jtext):
        jtext = self.P92_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"92.1 ^+X": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_93(self, jtext):
        jtext = self.P93_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"93.1 ^!MButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_93_12x(self, jtext):
        jtext = self.P93_12x.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"93.12x ^!MButton": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_96(self, jtext):
        jtext = self.P96_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"96.1 Tab & F5": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def UpdateKey_97(self, jtext):
        jtext = self.P97_1.toPlainText()
        if jtext != "":
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"97.1 Tab & F6": [jtext]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))




    def DefaultKey_1(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['1.1 +WheelDown'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"1.1 +WheelDown": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_2(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['2.1 +WheelUp'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"2.1 +WheelUp": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_3(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['3.1 #CapsLock'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"3.1 #CapsLock": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_4(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['4.1 !`'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"4.1 !`": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_7(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['7.1 Tab & Z'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"7.1 Tab & Z": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_10(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['10.1 MButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"10.1 MButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_11(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['11.1 +MButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"11.1 +MButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_12(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['12.1 +LButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"12.1 +LButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_13(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['13.1 +RButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"13.1 +RButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_14(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['14.1 ^MButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"14.1 ^MButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_15(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['15.1 CapsLock & 5'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"15.1 CapsLock & 5": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_16(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['16.1 +Capslock'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"16.1 +Capslock": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_17(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['17.1 ^Q'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"17.1 ^Q": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_18(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['18.1 ^!LButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"18.1 ^!LButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_19(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['19.1 ^!RButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"19.1 ^!RButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_20(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['20.1 ^+Q'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"20.1 ^+Q": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_22(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['22.1 CapsLock & RButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"22.1 CapsLock & RButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_23(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['23.1 CapsLock & LButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"23.1 CapsLock & LButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_24(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['24.1 +Tab'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"24.1 +Tab": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_25(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['25.1 CapsLock & MButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"25.1 CapsLock & MButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_33(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['33.1 CapsLock & `'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"33.1 CapsLock & `": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_34(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['34.12x CapsLock'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"34.12x CapsLock": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_36(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['36.1 Tab & S'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"36.1 Tab & S": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_37(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['37.1 Tab & W'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"37.1 Tab & W": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_38(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['38.1 Tab & A'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"38.1 Tab & A": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_39(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['39.1 Tab & D'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"39.1 Tab & D": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_41(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['41.1 +`'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"41.1 +`": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_42(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['42.1 Tab & Q'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"42.1 Tab & Q": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_47(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['47.1 Tab & F1'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"47.1 Tab & F1": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_48(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['48.1 Tab & F2'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"48.1 Tab & F2": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_49(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['49.1 Tab & F3'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"49.1 Tab & F3": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_50(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['50.1 Tab & F4'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"50.1 Tab & F4": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_51(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['51.1 CapsLock & 6'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"51.1 CapsLock & 6": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_52(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['52.12x Alt'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"52.12x Alt": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_53(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['53.1 !MButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"53.1 !MButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_54(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['54.1 !CapsLock'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"54.1 !CapsLock": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_55(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['55.1 !+LButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"55.1 !+LButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_56(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['56.1 !+RButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"56.1 !+RButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))


    def DefaultKey_58(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['58.1 `'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"58.1 `": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_59(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['59.1 ^+!MButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"59.1 ^+!MButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_64(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['64.1 Tab & 5'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"64.1 Tab & 5": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_65(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['65.1 Tab & 6'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"65.1 Tab & 6": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_67(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['67.1 CapsLock & 2'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"67.1 CapsLock & 2": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_68(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['68.1 CapsLock & 3'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"68.1 CapsLock & 3": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_69(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['69.1 CapsLock & 4'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"69.1 CapsLock & 4": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_70(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['70.1 CapsLock & Z'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"70.1 CapsLock & Z": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_72(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['72.1 ^+Space'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"72.1 ^+Space": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_73(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['73.1 CapsLock & R'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"73.1 CapsLock & R": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_74(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['74.1 CapsLock & E'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"74.1 CapsLock & E": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_76(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['76.1 CapsLock & F2'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"76.1 CapsLock & F2": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_86(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['86.1 ^+MButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"86.1 ^+MButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_87(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['87.1 !LButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"87.1 !LButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_88(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['88.1 ^Space'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"88.1 ^Space": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_89(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['89.1 ~Alt & ~Tab Up'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"89.1 ~Alt & ~Tab Up": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_90(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['90.1 Tab Tilde'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"90.1 Tab Tilde": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_91(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['91.1 ^x'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"91.1 ^x": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_92(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['92.1 ^+X'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"92.1 ^+X": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_93(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['93.1 ^!MButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"93.1 ^!MButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_93_12x(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['93.12x ^!MButton'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"93.12x ^!MButton": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_96(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['96.1 Tab & F5'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"96.1 Tab & F5": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))

    def DefaultKey_97(self):
        d_file = open(f"{basedir}\JSON DEFAULT.json", "r")
        json_object = json.load(d_file)
        d_file.close()
        dtext = f"{json_object['97.1 Tab & F6'][0]}"
        with open(f"{basedir}\JSON USER.json", "r") as f:
            key = json.load(f)
            key.update({"97.1 Tab & F6": [dtext]})
        with open(f"{basedir}\JSON USER.json", "w") as f:
            json.dump(key, f, indent=4, separators=(',', ': '))
