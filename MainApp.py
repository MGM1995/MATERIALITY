
import json
from ahk import AHK, Hotkey
from ahk.directives import NoTrayIcon
import os

basedir = os.path.dirname(__file__)


a_file = open(f"{basedir}\JSON USER.json", "r")
json_object = json.load(a_file)
a_file.close()



ahk = AHK(directives=[NoTrayIcon])
nl = '\n'
OUT = '"'
IN = '"'

AodobeString = f"if WinActive({IN}ahk_class {json_object['CONDITIONAL_2'][0]}{OUT}){nl}"
ExcelString = f"if WinActive({IN}ahk_class {json_object['CONDITIONAL_3'][0]}{OUT}){nl}"
WordString = f"if WinActive({IN}ahk_class {json_object['CONDITIONAL_4'][0]}{OUT}){nl}"
ElseString = f"else{nl}"
DoubleString = f"if (A_PriorHotkey = A_ThisHotkey) && (A_TimeSincePriorHotkey < 400){nl}"
CabinetString = f"if WinActive({IN}ahk_class CabinetWClass{OUT}){nl}"
ChromeString = f"if WinActive({IN}ahk_class {json_object['CONDITIONAL_5'][0]}{OUT}){nl}"


key_combo1 = "+WheelDown"
script1 = f"send {json_object['1.1 +WheelDown'][0]}"
hotkey1 = Hotkey(ahk, key_combo1, script1)

key_combo2 = "+WheelUp"
script2 = f"send {json_object['2.1 +WheelUp'][0]}"
hotkey2 = Hotkey(ahk, key_combo2, script2)

key_combo3 = "#CapsLock"
script3 = f"send {json_object['3.1 #CapsLock'][0]}"
hotkey3 = Hotkey(ahk, key_combo3, script3)

key_combo4 = "!`"
script4 = f"send {{text}}{json_object['4.1 !`'][0]}"
hotkey4 = Hotkey(ahk, key_combo4, script4)


key_combo5 = "Tab & WheelDown"
script5 = f"{WordString} send {json_object['5.4 Tab & WheelDown'][0]}{nl}{ExcelString} send {json_object['5.3 Tab & WheelDown'][0]}"
hotkey5 = Hotkey(ahk, key_combo5, script5)

key_combo6 = "~Tab & WheelUp"
script6 = f"{WordString} send {json_object['6.4 Tab & WheelUp'][0]}{nl}{ExcelString} send {json_object['6.3 Tab & WheelUp'][0]}"
hotkey6 = Hotkey(ahk, key_combo6, script6)


key_combo7 = "~Tab & Z"
script7 = f"{ExcelString} send {json_object['7.3 Tab & Z'][0]}{nl}{WordString} send {json_object['7.4 Tab & Z'][0]}{nl}{ElseString} send {json_object['7.1 Tab & Z'][0]}{nl}{AodobeString} send {json_object['7.2 Tab & Z'][0]}{nl}"
hotkey7 = Hotkey(ahk, key_combo7, script7)


key_combo8 = "~Tab & X"
script8 = f"{WordString} send {json_object['8.4 Tab & X'][0]}{nl}{AodobeString} send {json_object['8.2 Tab & X'][0]}{nl}{ExcelString} send {json_object['8.3 Tab & X'][0]}"
hotkey8 = Hotkey(ahk, key_combo8, script8)

key_combo9 = "~Tab & Space"
script9 = f"{ExcelString} send {json_object['9.3 Tab & Space'][0]}"
hotkey9 = Hotkey(ahk, key_combo9, script9)

key_combo10 = "MButton"
script10 = f"send {json_object['10.1 MButton'][0]}"
hotkey10 = Hotkey(ahk, key_combo10, script10)

key_combo11 = "+MButton"
script11 = f"{ExcelString} send {json_object['11.3 +MButton'][0]}{nl}{ChromeString} send {json_object['11.5 +MButton'][0]}{nl}{ElseString} send {json_object['11.1 +MButton'][0]}"
hotkey11 = Hotkey(ahk, key_combo11, script11)

key_combo12 = "+LButton"
script12 = f"{AodobeString} send {json_object['12.2 +LButton'][0]}{nl}{ElseString} send {json_object['12.1 +LButton'][0]}"
hotkey12 = Hotkey(ahk, key_combo12, script12)

key_combo13 = "+RButton"
script13 = f"{AodobeString} send {json_object['13.2 +RButton'][0]}{nl}{ElseString} send {json_object['13.1 +RButton'][0]}"
hotkey13 = Hotkey(ahk, key_combo13, script13)

key_combo14 = "^MButton"
script14 = f"{ChromeString} send {json_object['14.5 ^MButton'][0]}{nl}{ExcelString} send {json_object['14.3 ^MButton'][0]}{nl}{ElseString} send {json_object['14.1 ^MButton'][0]}"
hotkey14 = Hotkey(ahk, key_combo14, script14)

key_combo15 = "CapsLock & 5"
script15 = f"send {json_object['15.1 CapsLock & 5'][0]}"
hotkey15 = Hotkey(ahk, key_combo15, script15)

key_combo16 = "+Capslock"
script16 = f"{WordString} send {json_object['16.4 +Capslock'][0]}{nl}{ElseString} send {json_object['16.1 +Capslock'][0]}"
hotkey16 = Hotkey(ahk, key_combo16, script16)

key_combo17 = "^Q"
script17 = f"{ExcelString} send {json_object['17.3 ^Q'][0]}{nl}{CabinetString} return{nl}{ElseString} send {json_object['17.1 ^Q'][0]}"
hotkey17 = Hotkey(ahk, key_combo17, script17)

key_combo18 = "^!LButton"
script18 = f"send {json_object['18.1 ^!LButton'][0]}"
hotkey18 = Hotkey(ahk, key_combo18, script18)

key_combo19 = "^!RButton"
script19 = f"send {json_object['19.1 ^!RButton'][0]}"
hotkey19 = Hotkey(ahk, key_combo19, script19)

key_combo20 = "^+Q"
script20 = f"send {json_object['20.1 ^+Q'][0]}"
hotkey20 = Hotkey(ahk, key_combo20, script20)

key_combo21 = "^+F"
script21 = f"{ExcelString} send {json_object['21.3 ^+F'][0]}"
hotkey21 = Hotkey(ahk, key_combo21, script21)

key_combo22 = "~CapsLock & RButton"
script22 = f"{AodobeString} send {json_object['22.2 CapsLock & RButton'][0]}{nl}{ElseString} send {json_object['22.1 CapsLock & RButton'][0]}"
hotkey22 = Hotkey(ahk, key_combo22, script22)

key_combo23 = "~CapsLock & LButton"
script23 = f"{AodobeString} send {json_object['23.2 CapsLock & LButton'][0]}{nl}{ElseString} send {json_object['23.1 CapsLock & LButton'][0]}"
hotkey23 = Hotkey(ahk, key_combo23, script23)

key_combo24 = "Shift & ~Tab"
script24 = f"{ExcelString} send {json_object['24.3 +Tab'][0]}{nl}{WordString} send {json_object['24.4 +Tab'][0]}{nl}{ElseString} send {json_object['24.1 +Tab'][0]}"
hotkey24 = Hotkey(ahk, key_combo24, script24)

key_combo25 = "~CapsLock & MButton"
script25 = f"send {json_object['25.1 CapsLock & MButton'][0]}"
hotkey25 = Hotkey(ahk, key_combo25, script25)

key_combo26 = "~CapsLock & Q"
script26 = f"{ExcelString} send {json_object['26.3 CapsLock & Q'][0]}"
hotkey26 = Hotkey(ahk, key_combo26, script26)

key_combo27 = "~CapsLock & W"
script27 = f"{ExcelString} send {json_object['27.3 CapsLock & W'][0]}"
hotkey27 = Hotkey(ahk, key_combo27, script27)

key_combo28 = "~CapsLock & F"
script28 = f"{ExcelString} send {json_object['28.3 CapsLock & F'][0]}"
hotkey28 = Hotkey(ahk, key_combo28, script28)

key_combo29 = "~CapsLock & S"
script29 = f"{ExcelString} send {json_object['29.3 CapsLock & S'][0]}"
hotkey29 = Hotkey(ahk, key_combo29, script29)

key_combo30 = "~CapsLock & A"
script30 = f"{ExcelString} send {json_object['30.3 CapsLock & A'][0]}"
hotkey30 = Hotkey(ahk, key_combo30, script30)

key_combo31 = "~CapsLock & G"
script31 = f"{ExcelString} send {json_object['31.3 CapsLock & G'][0]}"
hotkey31 = Hotkey(ahk, key_combo31, script31)

key_combo32 = "~CapsLock & D"
script32 = f"{ExcelString} send {json_object['32.3 CapsLock & D'][0]}"
hotkey32 = Hotkey(ahk, key_combo32, script32)

key_combo33 = "~CapsLock & `"
script33 = f"{WordString} send {json_object['33.4 CapsLock & `'][0]}{nl}{ElseString} send {json_object['33.1 CapsLock & `'][0]}"
hotkey33 = Hotkey(ahk, key_combo33, script33)

key_combo34 = "~CapsLock Up"
script34 = f"{DoubleString} send {json_object['34.12x CapsLock'][0]}{nl}{ElseString}{json_object['34.0 CapsLock'][0]}"
hotkey34 = Hotkey(ahk, key_combo34, script34)

key_combo35 = "~Tab & 2"
script35 = f"{ExcelString} send {json_object['35.3 Tab & 2'][0]}"
hotkey35 = Hotkey(ahk, key_combo35, script35)

key_combo36 = "~Tab & S"
script36 = f"{ExcelString} {DoubleString}  send {json_object['36.32x Tab & S'][0]}{nl}{ElseString} send {json_object['36.1 Tab & S'][0]}"
hotkey36 = Hotkey(ahk, key_combo36, script36)

key_combo37 = "~Tab & W"
script37 = f"send {json_object['37.1 Tab & W'][0]}"
hotkey37 = Hotkey(ahk, key_combo37, script37)

key_combo38 = "~Tab & A"
script38 = f"send {json_object['38.1 Tab & A'][0]}"
hotkey38 = Hotkey(ahk, key_combo38, script38)

key_combo39 = "~Tab & D"
script39 = f"send {json_object['39.1 Tab & D'][0]}"
hotkey39 = Hotkey(ahk, key_combo39, script39)

key_combo40 = "~Tab & 3"
script40 = f"{ExcelString} send {json_object['40.3 Tab & 3'][0]}"
hotkey40 = Hotkey(ahk, key_combo40, script40)

key_combo41 = "+`"
script41 = f"{WordString} send {json_object['41.4 +`'][0]}{nl}{ElseString} send {json_object['41.1 +`'][0]}"
hotkey41 = Hotkey(ahk, key_combo41, script41)

key_combo42 = "~Tab & Q"
script42 = f"send {json_object['42.1 Tab & Q'][0]}"
hotkey42 = Hotkey(ahk, key_combo42, script42)

key_combo43 = "~Tab & RButton"
script43 = f"{AodobeString} send {json_object['43.2 Tab & RButton'][0]}{nl}{ExcelString} send {json_object['43.3 Tab & RButton'][0]}"
hotkey43 = Hotkey(ahk, key_combo43, script43)

key_combo44 = "~Tab & LButton"
script44 = f"{AodobeString} send {json_object['44.2 Tab & LButton'][0]}{nl}{ExcelString} send {json_object['44.3 Tab & LButton'][0]}"
hotkey44 = Hotkey(ahk, key_combo44, script44)

key_combo45 = "~Tab & MButton"
script45 = f"{ExcelString} send {json_object['45.3 Tab & MButton'][0]}{nl}{AodobeString} send {json_object['45.2 Tab & MButton'][0]}{nl}{ChromeString} send {json_object['45.5 Tab & MButton'][0]}"
hotkey45 = Hotkey(ahk, key_combo45, script45)


key_combo46 = "~Tab & 1"
script46 = f"{ExcelString} send {json_object['46.3 Tab & 1'][0]}"
hotkey46 = Hotkey(ahk, key_combo46, script46)

key_combo47 = "~Tab & F1"
script47 = f"send {json_object['47.1 Tab & F1'][0]}"
hotkey47 = Hotkey(ahk, key_combo47, script47)

key_combo48 = "~Tab & F2"
script48 = f"send {json_object['48.1 Tab & F2'][0]}"
hotkey48 = Hotkey(ahk, key_combo48, script48)

key_combo49 = "~Tab & F3"
script49 = f"send {json_object['49.1 Tab & F3'][0]}"
hotkey49 = Hotkey(ahk, key_combo49, script49)

key_combo50 = "~Tab & F4"
script50 = f"send {json_object['50.1 Tab & F4'][0]}"
hotkey50 = Hotkey(ahk, key_combo50, script50)

key_combo51 = "CapsLock & 6"
script51 = f"send {json_object['51.1 CapsLock & 6'][0]}"
hotkey51 = Hotkey(ahk, key_combo51, script51)

key_combo52 = "~Alt Up"
script52 = f"{DoubleString} send {json_object['52.12x Alt'][0]}"
hotkey52 = Hotkey(ahk, key_combo52, script52)

key_combo53 = "!MButton"
script53 = f"send {json_object['53.1 !MButton'][0]}"
hotkey53 = Hotkey(ahk, key_combo53, script53)

key_combo54 = "!CapsLock"
script54 = f"send {json_object['54.1 !CapsLock'][0]}{nl}{json_object['54.0 !CapsLock'][0]}"
hotkey54 = Hotkey(ahk, key_combo54, script54)

key_combo55 = "!+LButton"
script55 = f"send {json_object['55.1 !+LButton'][0]}"
hotkey55 = Hotkey(ahk, key_combo55, script55)

key_combo56 = "!+RButton"
script56 = f"send {json_object['56.1 !+RButton'][0]}"
hotkey56 = Hotkey(ahk, key_combo56, script56)

key_combo57 = "!+MButton"
script57 = f"{ExcelString} send {json_object['57.3 !+MButton'][0]}"
hotkey57 = Hotkey(ahk, key_combo57, script57)

key_combo58 = "`"
script58 = f"send {json_object['58.1 `'][0]}"
hotkey58 = Hotkey(ahk, key_combo58, script58)

key_combo59 = "^+!MButton"
script59 = f"send {json_object['59.1 ^+!MButton'][0]}"
hotkey59 = Hotkey(ahk, key_combo59, script59)

key_combo60 = "^W"
script60 = f"{WordString} send {json_object['60.4 ^W'][0]}"
hotkey60 = Hotkey(ahk, key_combo60, script60)

key_combo61 = "~Tab & R"
script61 = f"{WordString} send {json_object['61.4 Tab & R'][0]}"
hotkey61 = Hotkey(ahk, key_combo61, script61)

key_combo62 = "~Tab & T"
script62 = f"{WordString} send {json_object['62.4 Tab & T'][0]}"
hotkey62 = Hotkey(ahk, key_combo62, script62)

key_combo63 = "~Tab & 4"
script63 = f"{ExcelString} send {json_object['63.3 Tab & 4'][0]}"
hotkey63 = Hotkey(ahk, key_combo63, script63)

key_combo64 = "~Tab & 5"
script64 = f"{ExcelString} send {json_object['64.3 Tab & 5'][0]}{nl}{ElseString} send {json_object['64.1 Tab & 5'][0]}"
hotkey64 = Hotkey(ahk, key_combo64, script64)

key_combo65 = "~Tab & 6"
script65 = f"{ExcelString} send {json_object['65.3 Tab & 6'][0]}{nl}{ElseString} send {json_object['65.1 Tab & 6'][0]}"
hotkey65 = Hotkey(ahk, key_combo65, script65)

key_combo66 = "~CapsLock & 1"
script66 = f"{ExcelString} send {json_object['66.3 CapsLock & 1'][0]}"
hotkey66 = Hotkey(ahk, key_combo66, script66)

key_combo67 = "~CapsLock & 2"
script67 = f"send {json_object['67.1 CapsLock & 2'][0]}"
hotkey67 = Hotkey(ahk, key_combo67, script67)

key_combo68 = "~CapsLock & 3"
script68 = f"send {json_object['68.1 CapsLock & 3'][0]}"
hotkey68 = Hotkey(ahk, key_combo68, script68)

key_combo69 = "~CapsLock & 4"
script69 = f"send {json_object['69.1 CapsLock & 4'][0]}"
hotkey69 = Hotkey(ahk, key_combo69, script69)

key_combo70 = "~CapsLock & Z"
script70 = f"send {json_object['70.1 CapsLock & Z'][0]}{nl}{ChromeString} send {json_object['70.5 CapsLock & Z'][0]}"
hotkey70 = Hotkey(ahk, key_combo70, script70)

key_combo71 = "~CapsLock & X"
script71 = f"{ExcelString} send {json_object['71.3 CapsLock & X'][0]}{nl}{AodobeString} send {json_object['71.2 CapsLock & X'][0]}{nl}{WordString} send {json_object['71.4 CapsLock & X'][0]}{nl}{ChromeString} send {json_object['71.5 CapsLock & X'][0]}"
hotkey71 = Hotkey(ahk, key_combo71, script71)

key_combo72 = "^+Space"
script72 = f"send {json_object['72.1 ^+Space'][0]}"
hotkey72 = Hotkey(ahk, key_combo72, script72)

key_combo73 = "~CapsLock & R"
script73 = f"send {json_object['73.1 CapsLock & R'][0]}"
hotkey73 = Hotkey(ahk, key_combo73, script73)

key_combo74 = "~CapsLock & E"
script74 = f"send {json_object['74.1 CapsLock & E'][0]}"
hotkey74 = Hotkey(ahk, key_combo74, script74)

key_combo75 = "~CapsLock & F1"
script75 = f"{WordString} send {json_object['75.4 CapsLock & F1'][0]}"
hotkey75 = Hotkey(ahk, key_combo75, script75)

key_combo76 = "~CapsLock & F2"
script76 = f"send {json_object['76.1 CapsLock & F2'][0]}"
hotkey76 = Hotkey(ahk, key_combo76, script76)

key_combo77 = "~CapsLock & F3"
script77 = f"Run {json_object['77.6 CapsLock & F3'][0]}"
hotkey77 = Hotkey(ahk, key_combo77, script77)

key_combo78 = "~CapsLock & F4"
script78 = f"Run {json_object['78.6 CapsLock & F4'][0]}"
hotkey78 = Hotkey(ahk, key_combo78, script78)

key_combo79 = "~CapsLock & F5"
script79 = f"Run {json_object['79.6 CapsLock & F5'][0]}"
hotkey79 = Hotkey(ahk, key_combo79, script79)

key_combo80 = "~CapsLock & F6"
script80 = f"Run {json_object['80.6 CapsLock & F6'][0]}"
hotkey80 = Hotkey(ahk, key_combo80, script80)

key_combo81 = "~CapsLock & F7"
script81 = f"Run {json_object['81.6 CapsLock & F7'][0]}"
hotkey81 = Hotkey(ahk, key_combo81, script81)

key_combo82 = "~CapsLock & F8"
script82 = f"Run {json_object['82.6 CapsLock & F8'][0]}"
hotkey82 = Hotkey(ahk, key_combo82, script82)

key_combo83 = "~CapsLock & F9"
script83 = f"Run {json_object['83.6 CapsLock & F9'][0]}"
hotkey83 = Hotkey(ahk, key_combo83, script83)

key_combo84 = "~CapsLock & F10"
script84 = f"Run {json_object['84.6 CapsLock & F10'][0]}"
hotkey84 = Hotkey(ahk, key_combo84, script84)

key_combo85 = "~CapsLock & Space"
script85 = f"{ExcelString} send {json_object['85.3 CapsLock & Space'][0]}"
hotkey85 = Hotkey(ahk, key_combo85, script85)

key_combo86 = "^+MButton"
script86 = f"send {json_object['86.1 ^+MButton'][0]}"
hotkey86 = Hotkey(ahk, key_combo86, script86)

key_combo87 = "!LButton"
script87 = f"{ChromeString} send {json_object['87.5 !LButton'][0]}{nl}{ExcelString} send {json_object['87.3 !LButton'][0]}{nl}{ElseString} send {json_object['87.1 !LButton'][0]}"
hotkey87 = Hotkey(ahk, key_combo87, script87)

key_combo88 = "^Space"
script88 = f"{ExcelString} send {json_object['88.3 ^Space'][0]}{nl}{AodobeString} send {json_object['88.2 ^Space'][0]}{nl}{ElseString} send {json_object['88.1 ^Space'][0]}"
hotkey88 = Hotkey(ahk, key_combo88, script88)

key_combo89 = "~Alt & ~Tab Up"
script89 = f"send {json_object['89.1 ~Alt & ~Tab Up'][0]}"
hotkey89 = Hotkey(ahk, key_combo89, script89)

key_combo90 = "~Tab & `"
script90 = f"send {{text}}{json_object['90.1 Tab Tilde'][0]}"
hotkey90 = Hotkey(ahk, key_combo90, script90)

key_combo91 = "^x"
script91 = f"send {json_object['91.1 ^x'][0]}"
hotkey91 = Hotkey(ahk, key_combo91, script91)

key_combo92 = "^+X"
script92 = f"send {json_object['92.1 ^+X'][0]}"
hotkey92 = Hotkey(ahk, key_combo92, script92)

key_combo93 = "^!MButton"
script93 = f"{DoubleString} send {json_object['93.12x ^!MButton'][0]}{nl}{ElseString} send {json_object['93.1 ^!MButton'][0]}"
hotkey93 = Hotkey(ahk, key_combo93, script93)

key_combo94 = "~CapsLock & F11"
script94 = f"Run {json_object['94.6 CapsLock & F11'][0]}"
hotkey94 = Hotkey(ahk, key_combo94, script94)

key_combo95 = "~CapsLock & F12"
script95 = f"Run {json_object['95.6 CapsLock & F12'][0]}"
hotkey95 = Hotkey(ahk, key_combo95, script95)

key_combo96 = "~Tab & F5"
script96 = f"send {json_object['96.1 Tab & F5'][0]}"
hotkey96 = Hotkey(ahk, key_combo96, script96)

key_combo97 = "~Tab & F6"
script97 = f"send {json_object['97.1 Tab & F6'][0]}"
hotkey97 = Hotkey(ahk, key_combo97, script97)


def StopHotkeys():
    if (RUNTIME_DICT["HOTKEY_1"] == 1):
        hotkey1.stop()
    if (RUNTIME_DICT["HOTKEY_2"] == 1):
        hotkey2.stop()
    if (RUNTIME_DICT["HOTKEY_3"] == 1):
        hotkey3.stop()
    if (RUNTIME_DICT["HOTKEY_4"] == 1):
        hotkey4.stop()
    if (RUNTIME_DICT["HOTKEY_5"] == 1):
        hotkey5.stop()
    if (RUNTIME_DICT["HOTKEY_6"] == 1):
        hotkey6.stop()
    if (RUNTIME_DICT["HOTKEY_7"] == 1):
        hotkey7.stop()
    if (RUNTIME_DICT["HOTKEY_8"] == 1):
        hotkey8.stop()
    if (RUNTIME_DICT["HOTKEY_9"] == 1):
        hotkey9.stop()
    if (RUNTIME_DICT["HOTKEY_10"] == 1):
        hotkey10.stop()
    if (RUNTIME_DICT["HOTKEY_11"] == 1):
        hotkey11.stop()
    if (RUNTIME_DICT["HOTKEY_12"] == 1):
        hotkey12.stop()
    if (RUNTIME_DICT["HOTKEY_13"] == 1):
        hotkey13.stop()
    if (RUNTIME_DICT["HOTKEY_14"] == 1):
        hotkey14.stop()
    if (RUNTIME_DICT["HOTKEY_15"] == 1):
        hotkey15.stop()
    if (RUNTIME_DICT["HOTKEY_16"] == 1):
        hotkey16.stop()
    if (RUNTIME_DICT["HOTKEY_17"] == 1):
        hotkey17.stop()
    if (RUNTIME_DICT["HOTKEY_18"] == 1):
        hotkey18.stop()
    if (RUNTIME_DICT["HOTKEY_19"] == 1):
        hotkey19.stop()
    if (RUNTIME_DICT["HOTKEY_20"] == 1):
        hotkey20.stop()
    if (RUNTIME_DICT["HOTKEY_21"] == 1):
        hotkey21.stop()
    if (RUNTIME_DICT["HOTKEY_22"] == 1):
        hotkey22.stop()
    if (RUNTIME_DICT["HOTKEY_23"] == 1):
        hotkey23.stop()
    if (RUNTIME_DICT["HOTKEY_24"] == 1):
        hotkey24.stop()
    if (RUNTIME_DICT["HOTKEY_25"] == 1):
        hotkey25.stop()
    if (RUNTIME_DICT["HOTKEY_26"] == 1):
        hotkey26.stop()
    if (RUNTIME_DICT["HOTKEY_27"] == 1):
        hotkey27.stop()
    if (RUNTIME_DICT["HOTKEY_28"] == 1):
        hotkey28.stop()
    if (RUNTIME_DICT["HOTKEY_29"] == 1):
        hotkey29.stop()
    if (RUNTIME_DICT["HOTKEY_30"] == 1):
        hotkey30.stop()
    if (RUNTIME_DICT["HOTKEY_31"] == 1):
        hotkey31.stop()
    if (RUNTIME_DICT["HOTKEY_32"] == 1):
        hotkey32.stop()
    if (RUNTIME_DICT["HOTKEY_33"] == 1):
        hotkey33.stop()
    if (RUNTIME_DICT["HOTKEY_34"] == 1):
        hotkey34.stop()
    if (RUNTIME_DICT["HOTKEY_35"] == 1):
        hotkey35.stop()
    if (RUNTIME_DICT["HOTKEY_36"] == 1):
        hotkey36.stop()
    if (RUNTIME_DICT["HOTKEY_37"] == 1):
        hotkey37.stop()
    if (RUNTIME_DICT["HOTKEY_38"] == 1):
        hotkey38.stop()
    if (RUNTIME_DICT["HOTKEY_39"] == 1):
        hotkey39.stop()
    if (RUNTIME_DICT["HOTKEY_40"] == 1):
        hotkey40.stop()
    if (RUNTIME_DICT["HOTKEY_41"] == 1):
        hotkey41.stop()
    if (RUNTIME_DICT["HOTKEY_42"] == 1):
        hotkey42.stop()
    if (RUNTIME_DICT["HOTKEY_43"] == 1):
        hotkey43.stop()
    if (RUNTIME_DICT["HOTKEY_44"] == 1):
        hotkey44.stop()
    if (RUNTIME_DICT["HOTKEY_45"] == 1):
        hotkey45.stop()
    if (RUNTIME_DICT["HOTKEY_46"] == 1):
        hotkey46.stop()
    if (RUNTIME_DICT["HOTKEY_47"] == 1):
        hotkey47.stop()
    if (RUNTIME_DICT["HOTKEY_48"] == 1):
        hotkey48.stop()
    if (RUNTIME_DICT["HOTKEY_49"] == 1):
        hotkey49.stop()
    if (RUNTIME_DICT["HOTKEY_50"] == 1):
        hotkey50.stop()
    if (RUNTIME_DICT["HOTKEY_51"] == 1):
        hotkey51.stop()
    if (RUNTIME_DICT["HOTKEY_52"] == 1):
        hotkey52.stop()
    if (RUNTIME_DICT["HOTKEY_53"] == 1):
        hotkey53.stop()
    if (RUNTIME_DICT["HOTKEY_54"] == 1):
        hotkey54.stop()
    if (RUNTIME_DICT["HOTKEY_55"] == 1):
        hotkey55.stop()
    if (RUNTIME_DICT["HOTKEY_56"] == 1):
        hotkey56.stop()
    if (RUNTIME_DICT["HOTKEY_57"] == 1):
        hotkey57.stop()
    if (RUNTIME_DICT["HOTKEY_58"] == 1):
        hotkey58.stop()
    if (RUNTIME_DICT["HOTKEY_59"] == 1):
        hotkey59.stop()
    if (RUNTIME_DICT["HOTKEY_60"] == 1):
        hotkey60.stop()
    if (RUNTIME_DICT["HOTKEY_61"] == 1):
        hotkey61.stop()
    if (RUNTIME_DICT["HOTKEY_62"] == 1):
        hotkey62.stop()
    if (RUNTIME_DICT["HOTKEY_63"] == 1):
        hotkey63.stop()
    if (RUNTIME_DICT["HOTKEY_64"] == 1):
        hotkey64.stop()
    if (RUNTIME_DICT["HOTKEY_65"] == 1):
        hotkey65.stop()
    if (RUNTIME_DICT["HOTKEY_66"] == 1):
        hotkey66.stop()
    if (RUNTIME_DICT["HOTKEY_67"] == 1):
        hotkey67.stop()
    if (RUNTIME_DICT["HOTKEY_68"] == 1):
        hotkey68.stop()
    if (RUNTIME_DICT["HOTKEY_69"] == 1):
        hotkey69.stop()
    if (RUNTIME_DICT["HOTKEY_70"] == 1):
        hotkey70.stop()
    if (RUNTIME_DICT["HOTKEY_71"] == 1):
        hotkey71.stop()
    if (RUNTIME_DICT["HOTKEY_72"] == 1):
        hotkey72.stop()
    if (RUNTIME_DICT["HOTKEY_73"] == 1):
        hotkey73.stop()
    if (RUNTIME_DICT["HOTKEY_74"] == 1):
        hotkey74.stop()
    if (RUNTIME_DICT["HOTKEY_75"] == 1):
        hotkey75.stop()
    if (RUNTIME_DICT["HOTKEY_76"] == 1):
        hotkey76.stop()
    if (RUNTIME_DICT["HOTKEY_77"] == 1):
        hotkey77.stop()
    if (RUNTIME_DICT["HOTKEY_78"] == 1):
        hotkey78.stop()
    if (RUNTIME_DICT["HOTKEY_79"] == 1):
        hotkey79.stop()
    if (RUNTIME_DICT["HOTKEY_80"] == 1):
        hotkey80.stop()
    if (RUNTIME_DICT["HOTKEY_81"] == 1):
        hotkey81.stop()
    if (RUNTIME_DICT["HOTKEY_82"] == 1):
        hotkey82.stop()
    if (RUNTIME_DICT["HOTKEY_83"] == 1):
        hotkey83.stop()
    if (RUNTIME_DICT["HOTKEY_84"] == 1):
        hotkey84.stop()
    if (RUNTIME_DICT["HOTKEY_85"] == 1):
        hotkey85.stop()
    if (RUNTIME_DICT["HOTKEY_86"] == 1):
        hotkey86.stop()
    if (RUNTIME_DICT["HOTKEY_87"] == 1):
        hotkey87.stop()
    if (RUNTIME_DICT["HOTKEY_88"] == 1):
        hotkey88.stop()
    if (RUNTIME_DICT["HOTKEY_89"] == 1):
        hotkey89.stop()
    if (RUNTIME_DICT["HOTKEY_90"] == 1):
        hotkey90.stop()
    if (RUNTIME_DICT["HOTKEY_91"] == 1):
        hotkey91.stop()
    if (RUNTIME_DICT["HOTKEY_92"] == 1):
        hotkey92.stop()
    if (RUNTIME_DICT["HOTKEY_93"] == 1):
        hotkey93.stop()
    if (RUNTIME_DICT["HOTKEY_94"] == 1):
        hotkey94.stop()
    if (RUNTIME_DICT["HOTKEY_95"] == 1):
        hotkey95.stop()
    if (RUNTIME_DICT["HOTKEY_96"] == 1):
        hotkey96.stop()
    if (RUNTIME_DICT["HOTKEY_97"] == 1):
        hotkey97.stop()


def StartHotkeys():
    if f"{json_object['HOTKEY_1'][0]}" == "T":
        hotkey1.start()
        RUNTIME_DICT["HOTKEY_1"] = 1

    if f"{json_object['HOTKEY_2'][0]}" == "T":
        hotkey2.start()
        RUNTIME_DICT["HOTKEY_2"] = 1

    if f"{json_object['HOTKEY_3'][0]}" == "T":
        hotkey3.start()
        RUNTIME_DICT["HOTKEY_3"] = 1

    if f"{json_object['HOTKEY_4'][0]}" == "T":
        hotkey4.start()
        RUNTIME_DICT["HOTKEY_4"] = 1

    if f"{json_object['HOTKEY_5'][0]}" == "T":
        hotkey5.start()
        RUNTIME_DICT["HOTKEY_5"] = 1

    if f"{json_object['HOTKEY_6'][0]}" == "T":
        hotkey6.start()
        RUNTIME_DICT["HOTKEY_6"] = 1

    if f"{json_object['HOTKEY_7'][0]}" == "T":
        hotkey7.start()
        RUNTIME_DICT["HOTKEY_7"] = 1

    if f"{json_object['HOTKEY_8'][0]}" == "T":
        hotkey8.start()
        RUNTIME_DICT["HOTKEY_8"] = 1

    if f"{json_object['HOTKEY_9'][0]}" == "T":
        hotkey9.start()
        RUNTIME_DICT["HOTKEY_9"] = 1

    if f"{json_object['HOTKEY_10'][0]}" == "T":
        hotkey10.start()
        RUNTIME_DICT["HOTKEY_10"] = 1

    if f"{json_object['HOTKEY_11'][0]}" == "T":
        hotkey11.start()
        RUNTIME_DICT["HOTKEY_11"] = 1

    if f"{json_object['HOTKEY_12'][0]}" == "T":
        hotkey12.start()
        RUNTIME_DICT["HOTKEY_12"] = 1

    if f"{json_object['HOTKEY_13'][0]}" == "T":
        hotkey13.start()
        RUNTIME_DICT["HOTKEY_13"] = 1

    if f"{json_object['HOTKEY_14'][0]}" == "T":
        hotkey14.start()
        RUNTIME_DICT["HOTKEY_14"] = 1

    if f"{json_object['HOTKEY_15'][0]}" == "T":
        hotkey15.start()
        RUNTIME_DICT["HOTKEY_15"] = 1

    if f"{json_object['HOTKEY_16'][0]}" == "T":
        hotkey16.start()
        RUNTIME_DICT["HOTKEY_16"] = 1

    if f"{json_object['HOTKEY_17'][0]}" == "T":
        hotkey17.start()
        RUNTIME_DICT["HOTKEY_17"] = 1

    if f"{json_object['HOTKEY_18'][0]}" == "T":
        hotkey18.start()
        RUNTIME_DICT["HOTKEY_18"] = 1

    if f"{json_object['HOTKEY_19'][0]}" == "T":
        hotkey19.start()
        RUNTIME_DICT["HOTKEY_19"] = 1

    if f"{json_object['HOTKEY_20'][0]}" == "T":
        hotkey20.start()
        RUNTIME_DICT["HOTKEY_20"] = 1

    if f"{json_object['HOTKEY_21'][0]}" == "T":
        hotkey21.start()
        RUNTIME_DICT["HOTKEY_21"] = 1

    if f"{json_object['HOTKEY_22'][0]}" == "T":
        hotkey22.start()
        RUNTIME_DICT["HOTKEY_22"] = 1

    if f"{json_object['HOTKEY_23'][0]}" == "T":
        hotkey23.start()
        RUNTIME_DICT["HOTKEY_23"] = 1

    if f"{json_object['HOTKEY_24'][0]}" == "T":
        hotkey24.start()
        RUNTIME_DICT["HOTKEY_24"] = 1

    if f"{json_object['HOTKEY_25'][0]}" == "T":
        hotkey25.start()
        RUNTIME_DICT["HOTKEY_25"] = 1

    if f"{json_object['HOTKEY_26'][0]}" == "T":
        hotkey26.start()
        RUNTIME_DICT["HOTKEY_26"] = 1

    if f"{json_object['HOTKEY_27'][0]}" == "T":
        hotkey27.start()
        RUNTIME_DICT["HOTKEY_27"] = 1

    if f"{json_object['HOTKEY_28'][0]}" == "T":
        hotkey28.start()
        RUNTIME_DICT["HOTKEY_28"] = 1

    if f"{json_object['HOTKEY_29'][0]}" == "T":
        hotkey29.start()
        RUNTIME_DICT["HOTKEY_29"] = 1

    if f"{json_object['HOTKEY_30'][0]}" == "T":
        hotkey30.start()
        RUNTIME_DICT["HOTKEY_30"] = 1

    if f"{json_object['HOTKEY_31'][0]}" == "T":
        hotkey31.start()
        RUNTIME_DICT["HOTKEY_31"] = 1

    if f"{json_object['HOTKEY_32'][0]}" == "T":
        hotkey32.start()
        RUNTIME_DICT["HOTKEY_32"] = 1

    if f"{json_object['HOTKEY_33'][0]}" == "T":
        hotkey33.start()
        RUNTIME_DICT["HOTKEY_33"] = 1

    if f"{json_object['HOTKEY_34'][0]}" == "T":
        hotkey34.start()
        RUNTIME_DICT["HOTKEY_34"] = 1

    if f"{json_object['HOTKEY_35'][0]}" == "T":
        hotkey35.start()
        RUNTIME_DICT["HOTKEY_35"] = 1

    if f"{json_object['HOTKEY_36'][0]}" == "T":
        hotkey36.start()
        RUNTIME_DICT["HOTKEY_36"] = 1

    if f"{json_object['HOTKEY_37'][0]}" == "T":
        hotkey37.start()
        RUNTIME_DICT["HOTKEY_37"] = 1

    if f"{json_object['HOTKEY_38'][0]}" == "T":
        hotkey38.start()
        RUNTIME_DICT["HOTKEY_38"] = 1

    if f"{json_object['HOTKEY_39'][0]}" == "T":
        hotkey39.start()
        RUNTIME_DICT["HOTKEY_39"] = 1

    if f"{json_object['HOTKEY_40'][0]}" == "T":
        hotkey40.start()
        RUNTIME_DICT["HOTKEY_40"] = 1

    if f"{json_object['HOTKEY_41'][0]}" == "T":
        hotkey41.start()
        RUNTIME_DICT["HOTKEY_41"] = 1

    if f"{json_object['HOTKEY_42'][0]}" == "T":
        hotkey42.start()
        RUNTIME_DICT["HOTKEY_42"] = 1

    if f"{json_object['HOTKEY_43'][0]}" == "T":
        hotkey43.start()
        RUNTIME_DICT["HOTKEY_43"] = 1

    if f"{json_object['HOTKEY_44'][0]}" == "T":
        hotkey44.start()
        RUNTIME_DICT["HOTKEY_44"] = 1

    if f"{json_object['HOTKEY_45'][0]}" == "T":
        hotkey45.start()
        RUNTIME_DICT["HOTKEY_45"] = 1

    if f"{json_object['HOTKEY_46'][0]}" == "T":
        hotkey46.start()
        RUNTIME_DICT["HOTKEY_46"] = 1

    if f"{json_object['HOTKEY_47'][0]}" == "T":
        hotkey47.start()
        RUNTIME_DICT["HOTKEY_47"] = 1

    if f"{json_object['HOTKEY_48'][0]}" == "T":
        hotkey48.start()
        RUNTIME_DICT["HOTKEY_48"] = 1

    if f"{json_object['HOTKEY_49'][0]}" == "T":
        hotkey49.start()
        RUNTIME_DICT["HOTKEY_49"] = 1

    if f"{json_object['HOTKEY_50'][0]}" == "T":
        hotkey50.start()
        RUNTIME_DICT["HOTKEY_50"] = 1

    if f"{json_object['HOTKEY_51'][0]}" == "T":
        hotkey51.start()
        RUNTIME_DICT["HOTKEY_51"] = 1

    if f"{json_object['HOTKEY_52'][0]}" == "T":
        hotkey52.start()
        RUNTIME_DICT["HOTKEY_52"] = 1

    if f"{json_object['HOTKEY_53'][0]}" == "T":
        hotkey53.start()
        RUNTIME_DICT["HOTKEY_53"] = 1

    if f"{json_object['HOTKEY_54'][0]}" == "T":
        hotkey54.start()
        RUNTIME_DICT["HOTKEY_54"] = 1

    if f"{json_object['HOTKEY_55'][0]}" == "T":
        hotkey55.start()
        RUNTIME_DICT["HOTKEY_55"] = 1

    if f"{json_object['HOTKEY_56'][0]}" == "T":
        hotkey56.start()
        RUNTIME_DICT["HOTKEY_56"] = 1

    if f"{json_object['HOTKEY_57'][0]}" == "T":
        hotkey57.start()
        RUNTIME_DICT["HOTKEY_57"] = 1

    if f"{json_object['HOTKEY_58'][0]}" == "T":
        hotkey58.start()
        RUNTIME_DICT["HOTKEY_58"] = 1

    if f"{json_object['HOTKEY_59'][0]}" == "T":
        hotkey59.start()
        RUNTIME_DICT["HOTKEY_59"] = 1

    if f"{json_object['HOTKEY_60'][0]}" == "T":
        hotkey60.start()
        RUNTIME_DICT["HOTKEY_60"] = 1

    if f"{json_object['HOTKEY_61'][0]}" == "T":
        hotkey61.start()
        RUNTIME_DICT["HOTKEY_61"] = 1

    if f"{json_object['HOTKEY_62'][0]}" == "T":
        hotkey62.start()
        RUNTIME_DICT["HOTKEY_62"] = 1

    if f"{json_object['HOTKEY_63'][0]}" == "T":
        hotkey63.start()
        RUNTIME_DICT["HOTKEY_63"] = 1

    if f"{json_object['HOTKEY_64'][0]}" == "T":
        hotkey64.start()
        RUNTIME_DICT["HOTKEY_64"] = 1

    if f"{json_object['HOTKEY_65'][0]}" == "T":
        hotkey65.start()
        RUNTIME_DICT["HOTKEY_65"] = 1

    if f"{json_object['HOTKEY_66'][0]}" == "T":
        hotkey66.start()
        RUNTIME_DICT["HOTKEY_66"] = 1

    if f"{json_object['HOTKEY_67'][0]}" == "T":
        hotkey67.start()
        RUNTIME_DICT["HOTKEY_67"] = 1

    if f"{json_object['HOTKEY_68'][0]}" == "T":
        hotkey68.start()
        RUNTIME_DICT["HOTKEY_68"] = 1

    if f"{json_object['HOTKEY_69'][0]}" == "T":
        hotkey69.start()
        RUNTIME_DICT["HOTKEY_69"] = 1

    if f"{json_object['HOTKEY_70'][0]}" == "T":
        hotkey70.start()
        RUNTIME_DICT["HOTKEY_70"] = 1

    if f"{json_object['HOTKEY_71'][0]}" == "T":
        hotkey71.start()
        RUNTIME_DICT["HOTKEY_71"] = 1

    if f"{json_object['HOTKEY_72'][0]}" == "T":
        hotkey72.start()
        RUNTIME_DICT["HOTKEY_72"] = 1

    if f"{json_object['HOTKEY_73'][0]}" == "T":
        hotkey73.start()
        RUNTIME_DICT["HOTKEY_73"] = 1

    if f"{json_object['HOTKEY_74'][0]}" == "T":
        hotkey74.start()
        RUNTIME_DICT["HOTKEY_74"] = 1

    if f"{json_object['HOTKEY_75'][0]}" == "T":
        hotkey75.start()
        RUNTIME_DICT["HOTKEY_75"] = 1

    if f"{json_object['HOTKEY_76'][0]}" == "T":
        hotkey76.start()
        RUNTIME_DICT["HOTKEY_76"] = 1

    if f"{json_object['HOTKEY_77'][0]}" == "T":
        hotkey77.start()
        RUNTIME_DICT["HOTKEY_77"] = 1

    if f"{json_object['HOTKEY_78'][0]}" == "T":
        hotkey78.start()
        RUNTIME_DICT["HOTKEY_78"] = 1

    if f"{json_object['HOTKEY_79'][0]}" == "T":
        hotkey79.start()
        RUNTIME_DICT["HOTKEY_79"] = 1

    if f"{json_object['HOTKEY_80'][0]}" == "T":
        hotkey80.start()
        RUNTIME_DICT["HOTKEY_80"] = 1

    if f"{json_object['HOTKEY_81'][0]}" == "T":
        hotkey81.start()
        RUNTIME_DICT["HOTKEY_81"] = 1

    if f"{json_object['HOTKEY_82'][0]}" == "T":
        hotkey82.start()
        RUNTIME_DICT["HOTKEY_82"] = 1

    if f"{json_object['HOTKEY_83'][0]}" == "T":
        hotkey83.start()
        RUNTIME_DICT["HOTKEY_83"] = 1

    if f"{json_object['HOTKEY_84'][0]}" == "T":
        hotkey84.start()
        RUNTIME_DICT["HOTKEY_84"] = 1

    if f"{json_object['HOTKEY_85'][0]}" == "T":
        hotkey85.start()
        RUNTIME_DICT["HOTKEY_85"] = 1

    if f"{json_object['HOTKEY_86'][0]}" == "T":
        hotkey86.start()
        RUNTIME_DICT["HOTKEY_86"] = 1

    if f"{json_object['HOTKEY_87'][0]}" == "T":
        hotkey87.start()
        RUNTIME_DICT["HOTKEY_87"] = 1

    if f"{json_object['HOTKEY_88'][0]}" == "T":
        hotkey88.start()
        RUNTIME_DICT["HOTKEY_88"] = 1

    if f"{json_object['HOTKEY_89'][0]}" == "T":
        hotkey89.start()
        RUNTIME_DICT["HOTKEY_89"] = 1

    if f"{json_object['HOTKEY_90'][0]}" == "T":
        hotkey90.start()
        RUNTIME_DICT["HOTKEY_90"] = 1

    if f"{json_object['HOTKEY_91'][0]}" == "T":
        hotkey91.start()
        RUNTIME_DICT["HOTKEY_91"] = 1

    if f"{json_object['HOTKEY_92'][0]}" == "T":
        hotkey92.start()
        RUNTIME_DICT["HOTKEY_92"] = 1

    if f"{json_object['HOTKEY_93'][0]}" == "T":
        hotkey93.start()
        RUNTIME_DICT["HOTKEY_93"] = 1

    if f"{json_object['HOTKEY_94'][0]}" == "T":
        hotkey94.start()
        RUNTIME_DICT["HOTKEY_94"] = 1

    if f"{json_object['HOTKEY_95'][0]}" == "T":
        hotkey95.start()
        RUNTIME_DICT["HOTKEY_95"] = 1

    if f"{json_object['HOTKEY_96'][0]}" == "T":
        hotkey96.start()
        RUNTIME_DICT["HOTKEY_96"] = 1

    if f"{json_object['HOTKEY_97'][0]}" == "T":
        hotkey97.start()
        RUNTIME_DICT["HOTKEY_97"] = 1


ScriptList = [script1, script2, script3, script4, script5, script6, script7, script8, script9, script10, script11, script12,
              script13, script14, script15, script16, script17, script18, script19, script20, script21, script22, script23, script24, script25,
              script26, script27, script28, script29, script30, script31, script32, script33, script34, script35, script36, script37,
              script38, script39, script40, script41, script42, script43, script44, script45, script46, script47, script48, script49,
              script50, script51, script52, script53, script54, script55, script56, script57, script58, script59, script60, script61, script62,
              script63, script64, script65, script66, script67, script68, script69, script70, script71, script72, script73, script74,
              script75, script76, script77, script78, script79, script80, script81, script82, script83, script84, script85, script86,
              script87, script88, script89, script90, script91, script92, script93, script94, script95, script96, script97]


RUNTIME_DICT = {
    "HOTKEY_1": 0,
    "HOTKEY_2": 0,
    "HOTKEY_3": 0,
    "HOTKEY_4": 0,
    "HOTKEY_5": 0,
    "HOTKEY_6": 0,
    "HOTKEY_7": 0,
    "HOTKEY_8": 0,
    "HOTKEY_9": 0,
    "HOTKEY_10": 0,
    "HOTKEY_11": 0,
    "HOTKEY_12": 0,
    "HOTKEY_13": 0,
    "HOTKEY_14": 0,
    "HOTKEY_15": 0,
    "HOTKEY_16": 0,
    "HOTKEY_17": 0,
    "HOTKEY_18": 0,
    "HOTKEY_19": 0,
    "HOTKEY_20": 0,
    "HOTKEY_21": 0,
    "HOTKEY_22": 0,
    "HOTKEY_23": 0,
    "HOTKEY_24": 0,
    "HOTKEY_25": 0,
    "HOTKEY_26": 0,
    "HOTKEY_27": 0,
    "HOTKEY_28": 0,
    "HOTKEY_29": 0,
    "HOTKEY_30": 0,
    "HOTKEY_31": 0,
    "HOTKEY_32": 0,
    "HOTKEY_33": 0,
    "HOTKEY_34": 0,
    "HOTKEY_35": 0,
    "HOTKEY_36": 0,
    "HOTKEY_37": 0,
    "HOTKEY_38": 0,
    "HOTKEY_39": 0,
    "HOTKEY_40": 0,
    "HOTKEY_41": 0,
    "HOTKEY_42": 0,
    "HOTKEY_43": 0,
    "HOTKEY_44": 0,
    "HOTKEY_45": 0,
    "HOTKEY_46": 0,
    "HOTKEY_47": 0,
    "HOTKEY_48": 0,
    "HOTKEY_49": 0,
    "HOTKEY_50": 0,
    "HOTKEY_51": 0,
    "HOTKEY_52": 0,
    "HOTKEY_53": 0,
    "HOTKEY_54": 0,
    "HOTKEY_55": 0,
    "HOTKEY_56": 0,
    "HOTKEY_57": 0,
    "HOTKEY_58": 0,
    "HOTKEY_59": 0,
    "HOTKEY_60": 0,
    "HOTKEY_61": 0,
    "HOTKEY_62": 0,
    "HOTKEY_63": 0,
    "HOTKEY_64": 0,
    "HOTKEY_65": 0,
    "HOTKEY_66": 0,
    "HOTKEY_67": 0,
    "HOTKEY_68": 0,
    "HOTKEY_69": 0,
    "HOTKEY_70": 0,
    "HOTKEY_71": 0,
    "HOTKEY_72": 0,
    "HOTKEY_73": 0,
    "HOTKEY_74": 0,
    "HOTKEY_75": 0,
    "HOTKEY_76": 0,
    "HOTKEY_77": 0,
    "HOTKEY_78": 0,
    "HOTKEY_79": 0,
    "HOTKEY_80": 0,
    "HOTKEY_81": 0,
    "HOTKEY_82": 0,
    "HOTKEY_83": 0,
    "HOTKEY_84": 0,
    "HOTKEY_85": 0,
    "HOTKEY_86": 0,
    "HOTKEY_87": 0,
    "HOTKEY_88": 0,
    "HOTKEY_89": 0,
    "HOTKEY_90": 0,
    "HOTKEY_91": 0,
    "HOTKEY_92": 0,
    "HOTKEY_93": 0,
    "HOTKEY_94": 0,
    "HOTKEY_95": 0,
    "HOTKEY_96": 0,
    "HOTKEY_97": 0,
}

