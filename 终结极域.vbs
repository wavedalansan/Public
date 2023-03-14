P = msgbox("You only have one chance",0+48,"Warn")
X = msgbox("Confirm the closure of studentmain.exe?",1+32,"Inquire")
if X = vbOK Then
  Q = msgbox("Whether to clean up child processes?",1+32,"Inquire")
  if Q = vbOK Then
    CreateObject("WScript.Shell").Run "taskkill /F /IM studentmain.exe /T", 0
    X = msgbox("The program ended successfully				(At the same time, the child processes are cleaned up)",0+64,"Information")
else
    CreateObject("WScript.Shell").Run "taskkill /F /IM studentmain.exe", 0
    W = msgbox("The program ended successfully",0+64,"Information")
end if
else
  Y = msgbox("The operation has been canceled by the user",0+16,"Information")
end if