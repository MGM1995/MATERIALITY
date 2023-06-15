
import json
import os
from PyQt5.QtWidgets import QMainWindow, QFrame, QShortcut
from TOGGLE_OPTIONS_MENU import Ui_MainWindow
from PyQt5.QtGui import QKeySequence
import qtmodern.styles
import qtmodern.windows
from PyQt5.QtCore import pyqtSignal

basedir = os.path.dirname(__file__)
mw = 1



d_file = open(f"{basedir}\JSON USER.json", "r")
json_object = json.load(d_file)
d_file.close()


class TOGGLE_OPTIONS(QMainWindow, Ui_MainWindow):
    SaveSignal = pyqtSignal(int)
    DeactivateSignal = pyqtSignal(int)
    def __init__(self, *args, obj=None, **kwargs):
        super(TOGGLE_OPTIONS, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.UpdateCheckState()
        self.setWindowTitle("Preferences")
        self.SAVE_KEY_STATE_BTN.clicked.connect(self.CallConfigList)
        self.ACTIVATE_ALL_BTN.clicked.connect(self.CallActivateAll)
        self.DEACTIVATE_ALL_BTN.clicked.connect(self.CallDeactivateAll)
        self.PREFERENCES_SEARCH.textChanged.connect(self.SearchText)
        self.SaveShortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        self.SaveShortcut.activated.connect(self.CallConfigList)
        self.SearchShortcut = QShortcut(QKeySequence("Ctrl+F"), self)
        self.SearchShortcut.activated.connect(self.SelectFind)

    def ShowPreferncesModern(self):
        global mw
        mw = qtmodern.windows.ModernWindow(self)
        mw.showMaximized()
        mw.activateWindow()        
        

    def SearchText(self):
        jtext = (self.PREFERENCES_SEARCH.toPlainText()).lower()
        LabelList = [self.PL_1, self.PL_2, self.PL_3, self.PL_4, self.PL_5, self.PL_6, self.PL_7, self.PL_8,
                     self.PL_9, self.PL_10, self.PL_11, self.PL_12, self.PL_13, self.PL_14, self.PL_15, self.PL_16, self.PL_17,
                     self.PL_18, self.PL_19, self.PL_20, self.PL_21, self.PL_22, self.PL_23, self.PL_24, self.PL_25, self.PL_26,
                     self.PL_27, self.PL_28, self.PL_29, self.PL_30, self.PL_31, self.PL_32, self.PL_33, self.PL_34, self.PL_35,
                     self.PL_36, self.PL_37, self.PL_38, self.PL_39, self.PL_40, self.PL_41, self.PL_42, self.PL_43, self.PL_44,
                     self.PL_45, self.PL_46, self.PL_47, self.PL_48, self.PL_49, self.PL_50, self.PL_51, self.PL_52, self.PL_53,
                     self.PL_54, self.PL_55, self.PL_56, self.PL_57, self.PL_58, self.PL_59, self.PL_60, self.PL_61, self.PL_62,
                     self.PL_63, self.PL_64, self.PL_65, self.PL_66, self.PL_67, self.PL_68, self.PL_69, self.PL_70, self.PL_71,
                     self.PL_72, self.PL_73, self.PL_74, self.PL_75, self.PL_76, self.PL_77, self.PL_78, self.PL_79, self.PL_80,
                     self.PL_81, self.PL_82, self.PL_83, self.PL_84, self.PL_85, self.PL_86, self.PL_87, self.PL_88, self.PL_89,
                     self.PL_90, self.PL_91, self.PL_92, self.PL_93, self.PL_94, self.PL_95, self.PL_96, self.PL_97]
        for x in LabelList:
            if jtext == "":
                x.setFrameShape(QFrame.NoFrame)
            else:
                if jtext in x.text().lower():
                    x.setFrameShape(QFrame.WinPanel)
                else:
                    x.setFrameShape(QFrame.NoFrame)

    def SelectFind(self):
        self.PREFERENCES_SEARCH.setFocus()

    def CallActivateAll(self):
        ToggleList = [self.Toggle_1, self.Toggle_2, self.Toggle_3, self.Toggle_4, self.Toggle_5, self.Toggle_6, self.Toggle_7, self.Toggle_8,
                      self.Toggle_9, self.Toggle_10, self.Toggle_11, self.Toggle_12, self.Toggle_13, self.Toggle_14, self.Toggle_15, self.Toggle_16, self.Toggle_17, self.Toggle_18,
                      self.Toggle_19, self.Toggle_20, self.Toggle_21, self.Toggle_22, self.Toggle_23, self.Toggle_24, self.Toggle_25, self.Toggle_26, self.Toggle_27,
                      self.Toggle_28, self.Toggle_29, self.Toggle_30, self.Toggle_31, self.Toggle_32, self.Toggle_33, self.Toggle_34, self.Toggle_35, self.Toggle_36,
                      self.Toggle_37, self.Toggle_38, self.Toggle_39, self.Toggle_40, self.Toggle_41, self.Toggle_42, self.Toggle_43, self.Toggle_44, self.Toggle_45,
                      self.Toggle_46, self.Toggle_47, self.Toggle_48, self.Toggle_49, self.Toggle_50, self.Toggle_51, self.Toggle_52, self.Toggle_53, self.Toggle_54, self.Toggle_55, self.Toggle_56,
                      self.Toggle_57, self.Toggle_58, self.Toggle_59, self.Toggle_60, self.Toggle_61, self.Toggle_62, self.Toggle_63, self.Toggle_64, self.Toggle_65,
                      self.Toggle_66, self.Toggle_67, self.Toggle_68, self.Toggle_69, self.Toggle_70, self.Toggle_71, self.Toggle_72, self.Toggle_73, self.Toggle_74,
                      self.Toggle_75, self.Toggle_76, self.Toggle_77, self.Toggle_78, self.Toggle_79, self.Toggle_80, self.Toggle_81, self.Toggle_82, self.Toggle_83,
                      self.Toggle_84, self.Toggle_85, self.Toggle_86, self.Toggle_87, self.Toggle_88, self.Toggle_89, self.Toggle_90, self.Toggle_91, self.Toggle_92,
                      self.Toggle_93, self.Toggle_94, self.Toggle_95, self.Toggle_96, self.Toggle_97]
        for x in ToggleList:
            x.setCheckState(1)
        self.CallConfigList()
        self.SaveSignal.emit(1)            

    def CallDeactivateAll(self):
        ToggleList = [self.Toggle_1, self.Toggle_2, self.Toggle_3, self.Toggle_4, self.Toggle_5, self.Toggle_6, self.Toggle_7, self.Toggle_8,
                      self.Toggle_9, self.Toggle_10, self.Toggle_11, self.Toggle_12, self.Toggle_13, self.Toggle_14, self.Toggle_15, self.Toggle_16, self.Toggle_17, self.Toggle_18,
                      self.Toggle_19, self.Toggle_20, self.Toggle_21, self.Toggle_22, self.Toggle_23, self.Toggle_24, self.Toggle_25, self.Toggle_26, self.Toggle_27,
                      self.Toggle_28, self.Toggle_29, self.Toggle_30, self.Toggle_31, self.Toggle_32, self.Toggle_33, self.Toggle_34, self.Toggle_35, self.Toggle_36,
                      self.Toggle_37, self.Toggle_38, self.Toggle_39, self.Toggle_40, self.Toggle_41, self.Toggle_42, self.Toggle_43, self.Toggle_44, self.Toggle_45,
                      self.Toggle_46, self.Toggle_47, self.Toggle_48, self.Toggle_49, self.Toggle_50, self.Toggle_51, self.Toggle_52, self.Toggle_53, self.Toggle_54, self.Toggle_55,
                      self.Toggle_56, self.Toggle_57, self.Toggle_58, self.Toggle_59, self.Toggle_60, self.Toggle_61, self.Toggle_62, self.Toggle_63, self.Toggle_64,
                      self.Toggle_65, self.Toggle_66, self.Toggle_67, self.Toggle_68, self.Toggle_69, self.Toggle_70, self.Toggle_71, self.Toggle_72, self.Toggle_73,
                      self.Toggle_74, self.Toggle_75, self.Toggle_76, self.Toggle_77, self.Toggle_78, self.Toggle_79, self.Toggle_80, self.Toggle_81, self.Toggle_82,
                      self.Toggle_83, self.Toggle_84, self.Toggle_85, self.Toggle_86, self.Toggle_87, self.Toggle_88, self.Toggle_89, self.Toggle_90, self.Toggle_91,
                      self.Toggle_92, self.Toggle_93, self.Toggle_94, self.Toggle_95, self.Toggle_96, self.Toggle_97]
        for x in ToggleList:
            x.setCheckState(0)
        self.CallConfigList()
        self.DeactivateSignal.emit(1)            

    def UpdateCheckState(self):
        if f"{json_object['HOTKEY_1'][0]}" == "T":
            self.Toggle_1.setCheckState(1)

        if f"{json_object['HOTKEY_2'][0]}" == "T":
            self.Toggle_2.setCheckState(1)

        if f"{json_object['HOTKEY_3'][0]}" == "T":
            self.Toggle_3.setCheckState(1)

        if f"{json_object['HOTKEY_4'][0]}" == "T":
            self.Toggle_4.setCheckState(1)

        if f"{json_object['HOTKEY_5'][0]}" == "T":
            self.Toggle_5.setCheckState(1)

        if f"{json_object['HOTKEY_6'][0]}" == "T":
            self.Toggle_6.setCheckState(1)

        if f"{json_object['HOTKEY_7'][0]}" == "T":
            self.Toggle_7.setCheckState(1)

        if f"{json_object['HOTKEY_8'][0]}" == "T":
            self.Toggle_8.setCheckState(1)

        if f"{json_object['HOTKEY_9'][0]}" == "T":
            self.Toggle_9.setCheckState(1)

        if f"{json_object['HOTKEY_10'][0]}" == "T":
            self.Toggle_10.setCheckState(1)

        if f"{json_object['HOTKEY_11'][0]}" == "T":
            self.Toggle_11.setCheckState(1)

        if f"{json_object['HOTKEY_12'][0]}" == "T":
            self.Toggle_12.setCheckState(1)

        if f"{json_object['HOTKEY_13'][0]}" == "T":
            self.Toggle_13.setCheckState(1)

        if f"{json_object['HOTKEY_14'][0]}" == "T":
            self.Toggle_14.setCheckState(1)

        if f"{json_object['HOTKEY_15'][0]}" == "T":
            self.Toggle_15.setCheckState(1)

        if f"{json_object['HOTKEY_16'][0]}" == "T":
            self.Toggle_16.setCheckState(1)

        if f"{json_object['HOTKEY_17'][0]}" == "T":
            self.Toggle_17.setCheckState(1)

        if f"{json_object['HOTKEY_18'][0]}" == "T":
            self.Toggle_18.setCheckState(1)

        if f"{json_object['HOTKEY_19'][0]}" == "T":
            self.Toggle_19.setCheckState(1)

        if f"{json_object['HOTKEY_20'][0]}" == "T":
            self.Toggle_20.setCheckState(1)

        if f"{json_object['HOTKEY_21'][0]}" == "T":
            self.Toggle_21.setCheckState(1)

        if f"{json_object['HOTKEY_22'][0]}" == "T":
            self.Toggle_22.setCheckState(1)

        if f"{json_object['HOTKEY_23'][0]}" == "T":
            self.Toggle_23.setCheckState(1)

        if f"{json_object['HOTKEY_24'][0]}" == "T":
            self.Toggle_24.setCheckState(1)

        if f"{json_object['HOTKEY_25'][0]}" == "T":
            self.Toggle_25.setCheckState(1)

        if f"{json_object['HOTKEY_26'][0]}" == "T":
            self.Toggle_26.setCheckState(1)

        if f"{json_object['HOTKEY_27'][0]}" == "T":
            self.Toggle_27.setCheckState(1)

        if f"{json_object['HOTKEY_28'][0]}" == "T":
            self.Toggle_28.setCheckState(1)

        if f"{json_object['HOTKEY_29'][0]}" == "T":
            self.Toggle_29.setCheckState(1)

        if f"{json_object['HOTKEY_30'][0]}" == "T":
            self.Toggle_30.setCheckState(1)

        if f"{json_object['HOTKEY_31'][0]}" == "T":
            self.Toggle_31.setCheckState(1)

        if f"{json_object['HOTKEY_32'][0]}" == "T":
            self.Toggle_32.setCheckState(1)

        if f"{json_object['HOTKEY_33'][0]}" == "T":
            self.Toggle_33.setCheckState(1)

        if f"{json_object['HOTKEY_34'][0]}" == "T":
            self.Toggle_34.setCheckState(1)

        if f"{json_object['HOTKEY_35'][0]}" == "T":
            self.Toggle_35.setCheckState(1)

        if f"{json_object['HOTKEY_36'][0]}" == "T":
            self.Toggle_36.setCheckState(1)

        if f"{json_object['HOTKEY_37'][0]}" == "T":
            self.Toggle_37.setCheckState(1)

        if f"{json_object['HOTKEY_38'][0]}" == "T":
            self.Toggle_38.setCheckState(1)

        if f"{json_object['HOTKEY_39'][0]}" == "T":
            self.Toggle_39.setCheckState(1)

        if f"{json_object['HOTKEY_40'][0]}" == "T":
            self.Toggle_40.setCheckState(1)

        if f"{json_object['HOTKEY_41'][0]}" == "T":
            self.Toggle_41.setCheckState(1)

        if f"{json_object['HOTKEY_42'][0]}" == "T":
            self.Toggle_42.setCheckState(1)

        if f"{json_object['HOTKEY_43'][0]}" == "T":
            self.Toggle_43.setCheckState(1)

        if f"{json_object['HOTKEY_44'][0]}" == "T":
            self.Toggle_44.setCheckState(1)

        if f"{json_object['HOTKEY_45'][0]}" == "T":
            self.Toggle_45.setCheckState(1)

        if f"{json_object['HOTKEY_46'][0]}" == "T":
            self.Toggle_46.setCheckState(1)

        if f"{json_object['HOTKEY_47'][0]}" == "T":
            self.Toggle_47.setCheckState(1)

        if f"{json_object['HOTKEY_48'][0]}" == "T":
            self.Toggle_48.setCheckState(1)

        if f"{json_object['HOTKEY_49'][0]}" == "T":
            self.Toggle_49.setCheckState(1)

        if f"{json_object['HOTKEY_50'][0]}" == "T":
            self.Toggle_50.setCheckState(1)

        if f"{json_object['HOTKEY_51'][0]}" == "T":
            self.Toggle_51.setCheckState(1)

        if f"{json_object['HOTKEY_52'][0]}" == "T":
            self.Toggle_52.setCheckState(1)

        if f"{json_object['HOTKEY_53'][0]}" == "T":
            self.Toggle_53.setCheckState(1)

        if f"{json_object['HOTKEY_54'][0]}" == "T":
            self.Toggle_54.setCheckState(1)

        if f"{json_object['HOTKEY_55'][0]}" == "T":
            self.Toggle_55.setCheckState(1)

        if f"{json_object['HOTKEY_56'][0]}" == "T":
            self.Toggle_56.setCheckState(1)

        if f"{json_object['HOTKEY_57'][0]}" == "T":
            self.Toggle_57.setCheckState(1)

        if f"{json_object['HOTKEY_58'][0]}" == "T":
            self.Toggle_58.setCheckState(1)

        if f"{json_object['HOTKEY_59'][0]}" == "T":
            self.Toggle_59.setCheckState(1)

        if f"{json_object['HOTKEY_60'][0]}" == "T":
            self.Toggle_60.setCheckState(1)

        if f"{json_object['HOTKEY_61'][0]}" == "T":
            self.Toggle_61.setCheckState(1)

        if f"{json_object['HOTKEY_62'][0]}" == "T":
            self.Toggle_62.setCheckState(1)

        if f"{json_object['HOTKEY_63'][0]}" == "T":
            self.Toggle_63.setCheckState(1)

        if f"{json_object['HOTKEY_64'][0]}" == "T":
            self.Toggle_64.setCheckState(1)

        if f"{json_object['HOTKEY_65'][0]}" == "T":
            self.Toggle_65.setCheckState(1)

        if f"{json_object['HOTKEY_66'][0]}" == "T":
            self.Toggle_66.setCheckState(1)

        if f"{json_object['HOTKEY_67'][0]}" == "T":
            self.Toggle_67.setCheckState(1)

        if f"{json_object['HOTKEY_68'][0]}" == "T":
            self.Toggle_68.setCheckState(1)

        if f"{json_object['HOTKEY_69'][0]}" == "T":
            self.Toggle_69.setCheckState(1)

        if f"{json_object['HOTKEY_70'][0]}" == "T":
            self.Toggle_70.setCheckState(1)

        if f"{json_object['HOTKEY_71'][0]}" == "T":
            self.Toggle_71.setCheckState(1)

        if f"{json_object['HOTKEY_72'][0]}" == "T":
            self.Toggle_72.setCheckState(1)

        if f"{json_object['HOTKEY_73'][0]}" == "T":
            self.Toggle_73.setCheckState(1)

        if f"{json_object['HOTKEY_74'][0]}" == "T":
            self.Toggle_74.setCheckState(1)

        if f"{json_object['HOTKEY_75'][0]}" == "T":
            self.Toggle_75.setCheckState(1)

        if f"{json_object['HOTKEY_76'][0]}" == "T":
            self.Toggle_76.setCheckState(1)

        if f"{json_object['HOTKEY_77'][0]}" == "T":
            self.Toggle_77.setCheckState(1)

        if f"{json_object['HOTKEY_78'][0]}" == "T":
            self.Toggle_78.setCheckState(1)

        if f"{json_object['HOTKEY_79'][0]}" == "T":
            self.Toggle_79.setCheckState(1)

        if f"{json_object['HOTKEY_80'][0]}" == "T":
            self.Toggle_80.setCheckState(1)

        if f"{json_object['HOTKEY_81'][0]}" == "T":
            self.Toggle_81.setCheckState(1)

        if f"{json_object['HOTKEY_82'][0]}" == "T":
            self.Toggle_82.setCheckState(1)

        if f"{json_object['HOTKEY_83'][0]}" == "T":
            self.Toggle_83.setCheckState(1)

        if f"{json_object['HOTKEY_84'][0]}" == "T":
            self.Toggle_84.setCheckState(1)

        if f"{json_object['HOTKEY_85'][0]}" == "T":
            self.Toggle_85.setCheckState(1)

        if f"{json_object['HOTKEY_86'][0]}" == "T":
            self.Toggle_86.setCheckState(1)

        if f"{json_object['HOTKEY_87'][0]}" == "T":
            self.Toggle_87.setCheckState(1)

        if f"{json_object['HOTKEY_88'][0]}" == "T":
            self.Toggle_88.setCheckState(1)

        if f"{json_object['HOTKEY_89'][0]}" == "T":
            self.Toggle_89.setCheckState(1)

        if f"{json_object['HOTKEY_90'][0]}" == "T":
            self.Toggle_90.setCheckState(1)

        if f"{json_object['HOTKEY_91'][0]}" == "T":
            self.Toggle_91.setCheckState(1)

        if f"{json_object['HOTKEY_92'][0]}" == "T":
            self.Toggle_92.setCheckState(1)

        if f"{json_object['HOTKEY_93'][0]}" == "T":
            self.Toggle_93.setCheckState(1)

        if f"{json_object['HOTKEY_94'][0]}" == "T":
            self.Toggle_94.setCheckState(1)

        if f"{json_object['HOTKEY_95'][0]}" == "T":
            self.Toggle_95.setCheckState(1)

        if f"{json_object['HOTKEY_96'][0]}" == "T":
            self.Toggle_96.setCheckState(1)

        if f"{json_object['HOTKEY_97'][0]}" == "T":
            self.Toggle_97.setCheckState(1)
        
        if f"{json_object['MinStart_S'][0]}" == "T":
            self.MinStart.setCheckState(2)

    def CallConfigList(self):
        ConfigList = [self.ConfigKey_1, self.ConfigKey_2, self.ConfigKey_3, self.ConfigKey_4, self.ConfigKey_5, self.ConfigKey_6,
                      self.ConfigKey_7, self.ConfigKey_8, self.ConfigKey_9, self.ConfigKey_10, self.ConfigKey_11, self.ConfigKey_12, self.ConfigKey_13,
                      self.ConfigKey_14, self.ConfigKey_15, self.ConfigKey_16, self.ConfigKey_17, self.ConfigKey_18, self.ConfigKey_19, self.ConfigKey_20, self.ConfigKey_21,
                      self.ConfigKey_22, self.ConfigKey_23, self.ConfigKey_24, self.ConfigKey_25, self.ConfigKey_26, self.ConfigKey_27, self.ConfigKey_28,
                      self.ConfigKey_29, self.ConfigKey_30, self.ConfigKey_31, self.ConfigKey_32, self.ConfigKey_33, self.ConfigKey_34, self.ConfigKey_35,
                      self.ConfigKey_36, self.ConfigKey_37, self.ConfigKey_38, self.ConfigKey_39, self.ConfigKey_40, self.ConfigKey_41, self.ConfigKey_42,
                      self.ConfigKey_43, self.ConfigKey_44, self.ConfigKey_45, self.ConfigKey_46, self.ConfigKey_47, self.ConfigKey_48, self.ConfigKey_49,
                      self.ConfigKey_50, self.ConfigKey_51, self.ConfigKey_52, self.ConfigKey_53, self.ConfigKey_54, self.ConfigKey_55, self.ConfigKey_56, self.ConfigKey_57,
                      self.ConfigKey_58, self.ConfigKey_59, self.ConfigKey_60, self.ConfigKey_61, self.ConfigKey_62, self.ConfigKey_63, self.ConfigKey_64,
                      self.ConfigKey_65, self.ConfigKey_66, self.ConfigKey_67, self.ConfigKey_68, self.ConfigKey_69, self.ConfigKey_70, self.ConfigKey_71,
                      self.ConfigKey_72, self.ConfigKey_73, self.ConfigKey_74, self.ConfigKey_75, self.ConfigKey_76, self.ConfigKey_77, self.ConfigKey_78,
                      self.ConfigKey_79, self.ConfigKey_80, self.ConfigKey_81, self.ConfigKey_82, self.ConfigKey_83, self.ConfigKey_84, self.ConfigKey_85,
                      self.ConfigKey_86, self.ConfigKey_87, self.ConfigKey_88, self.ConfigKey_89, self.ConfigKey_90, self.ConfigKey_91, self.ConfigKey_92,
                      self.ConfigKey_93, self.ConfigKey_94, self.ConfigKey_95, self.ConfigKey_96, self.ConfigKey_97, self.CallMinStart]
        for x in ConfigList:
            x()
        self.SaveSignal.emit(1)     


    def ConfigKey_1(self):
        if self.Toggle_1.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_1": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_1": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_2(self):
        if self.Toggle_2.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_2": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_2": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_3(self):
        if self.Toggle_3.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_3": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_3": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_4(self):
        if self.Toggle_4.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_4": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_4": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_5(self):
        if self.Toggle_5.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_5": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_5": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_6(self):
        if self.Toggle_6.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_6": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_6": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_7(self):
        if self.Toggle_7.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_7": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_7": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_8(self):
        if self.Toggle_8.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_8": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_8": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_9(self):
        if self.Toggle_9.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_9": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_9": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_10(self):
        if self.Toggle_10.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_10": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_10": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_11(self):
        if self.Toggle_11.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_11": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_11": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_12(self):
        if self.Toggle_12.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_12": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_12": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_13(self):
        if self.Toggle_13.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_13": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_13": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_14(self):
        if self.Toggle_14.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_14": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_14": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_15(self):
        if self.Toggle_15.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_15": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_15": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_16(self):
        if self.Toggle_16.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_16": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_16": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_17(self):
        if self.Toggle_17.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_17": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_17": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_18(self):
        if self.Toggle_18.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_18": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_18": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_19(self):
        if self.Toggle_19.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_19": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_19": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_20(self):
        if self.Toggle_20.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_20": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_20": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_21(self):
        if self.Toggle_21.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_21": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_21": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_22(self):
        if self.Toggle_22.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_22": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_22": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_23(self):
        if self.Toggle_23.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_23": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_23": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_24(self):
        if self.Toggle_24.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_24": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_24": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_25(self):
        if self.Toggle_25.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_25": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_25": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_26(self):
        if self.Toggle_26.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_26": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_26": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_27(self):
        if self.Toggle_27.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_27": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_27": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_28(self):
        if self.Toggle_28.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_28": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_28": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_29(self):
        if self.Toggle_29.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_29": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_29": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_30(self):
        if self.Toggle_30.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_30": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_30": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_31(self):
        if self.Toggle_31.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_31": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_31": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_32(self):
        if self.Toggle_32.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_32": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_32": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_33(self):
        if self.Toggle_33.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_33": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_33": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_34(self):
        if self.Toggle_34.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_34": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_34": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_35(self):
        if self.Toggle_35.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_35": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_35": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_36(self):
        if self.Toggle_36.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_36": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_36": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_37(self):
        if self.Toggle_37.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_37": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_37": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_38(self):
        if self.Toggle_38.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_38": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_38": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_39(self):
        if self.Toggle_39.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_39": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_39": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_40(self):
        if self.Toggle_40.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_40": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_40": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_41(self):
        if self.Toggle_41.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_41": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_41": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_42(self):
        if self.Toggle_42.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_42": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_42": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_43(self):
        if self.Toggle_43.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_43": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_43": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_44(self):
        if self.Toggle_44.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_44": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_44": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_45(self):
        if self.Toggle_45.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_45": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_45": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_46(self):
        if self.Toggle_46.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_46": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_46": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_47(self):
        if self.Toggle_47.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_47": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_47": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_48(self):
        if self.Toggle_48.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_48": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_48": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_49(self):
        if self.Toggle_49.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_49": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_49": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_50(self):
        if self.Toggle_50.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_50": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_50": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_51(self):
        if self.Toggle_51.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_51": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_51": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_52(self):
        if self.Toggle_52.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_52": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_52": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_53(self):
        if self.Toggle_53.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_53": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_53": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_54(self):
        if self.Toggle_54.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_54": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_54": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_55(self):
        if self.Toggle_55.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_55": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_55": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_56(self):
        if self.Toggle_56.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_56": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_56": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_57(self):
        if self.Toggle_57.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_57": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_57": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_58(self):
        if self.Toggle_58.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_58": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_58": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_59(self):
        if self.Toggle_59.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_59": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_59": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_60(self):
        if self.Toggle_60.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_60": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_60": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_61(self):
        if self.Toggle_61.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_61": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_61": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_62(self):
        if self.Toggle_62.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_62": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_62": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_63(self):
        if self.Toggle_63.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_63": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_63": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_64(self):
        if self.Toggle_64.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_64": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_64": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_65(self):
        if self.Toggle_65.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_65": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_65": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_66(self):
        if self.Toggle_66.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_66": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_66": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_67(self):
        if self.Toggle_67.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_67": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_67": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_68(self):
        if self.Toggle_68.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_68": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_68": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_69(self):
        if self.Toggle_69.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_69": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_69": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_70(self):
        if self.Toggle_70.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_70": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_70": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_71(self):
        if self.Toggle_71.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_71": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_71": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_72(self):
        if self.Toggle_72.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_72": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_72": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_73(self):
        if self.Toggle_73.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_73": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_73": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_74(self):
        if self.Toggle_74.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_74": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_74": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_75(self):
        if self.Toggle_75.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_75": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_75": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_76(self):
        if self.Toggle_76.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_76": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_76": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_77(self):
        if self.Toggle_77.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_77": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_77": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_78(self):
        if self.Toggle_78.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_78": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_78": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_79(self):
        if self.Toggle_79.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_79": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_79": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_80(self):
        if self.Toggle_80.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_80": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_80": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_81(self):
        if self.Toggle_81.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_81": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_81": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_82(self):
        if self.Toggle_82.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_82": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_82": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_83(self):
        if self.Toggle_83.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_83": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_83": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_84(self):
        if self.Toggle_84.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_84": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_84": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_85(self):
        if self.Toggle_85.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_85": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_85": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_86(self):
        if self.Toggle_86.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_86": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_86": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_87(self):
        if self.Toggle_87.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_87": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_87": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_88(self):
        if self.Toggle_88.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_88": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_88": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_89(self):
        if self.Toggle_89.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_89": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_89": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_90(self):
        if self.Toggle_90.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_90": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_90": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_91(self):
        if self.Toggle_91.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_91": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_91": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_92(self):
        if self.Toggle_92.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_92": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_92": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_93(self):
        if self.Toggle_93.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_93": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_93": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_94(self):
        if self.Toggle_94.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_94": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_94": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_95(self):
        if self.Toggle_95.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_95": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_95": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_96(self):
        if self.Toggle_96.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_96": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_96": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def ConfigKey_97(self):
        if self.Toggle_97.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_97": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"HOTKEY_97": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))

    def CallMinStart(self):
        if self.MinStart.isChecked():
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"MinStart_S": ["T"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
        else:
            with open(f"{basedir}\JSON USER.json", "r") as f:
                key = json.load(f)
                key.update({"MinStart_S": ["F"]})
            with open(f"{basedir}\JSON USER.json", "w") as f:
                json.dump(key, f, indent=4, separators=(',', ': '))
