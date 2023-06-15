Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c TerminateAHK"
oShell.Run strArgs, 0, false