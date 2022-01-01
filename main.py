import ctypes
import time
import os

ctypes.windll.kernel32.SetConsoleTitleW("View Counter")

os.system("cls")
i = 0

while 0 == 0:
    print("Getting Views")
    os.system("views.js > views")
    f = open("views", "r")
    views = f.read()
    f.close()
    
    print("Making Image")
    os.system("image.bat " + views)
    
    print("Uploading Img")
    os.system("update.js")
    
    print("Done! " + str(i))
    print("60sec Timeout")
    time.sleep(60)
    os.system("cls")
    i+=1