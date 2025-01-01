import serial
import time
import os

SerialObj = serial.Serial('COM4')
                                   
SerialObj.baudrate = 9600  
SerialObj.bytesize = 8     
SerialObj.parity   ='N'    
SerialObj.stopbits = 1     

SerialObj.timeout  = None

print('Prev = Log out')
print('Next = Restart')
print('Play = Shut Down')

time.sleep(1)  

ReceivedString = SerialObj.readline()

if ReceivedString == b'a\r\n':
    os.system("shutdown /s /t 3")
    print('Shutting down in 3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
elif ReceivedString == b'b\r\n':
    os.system("shutdown /r /t 3")
    print('Restarting in 3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
elif ReceivedString == b'c\r\n':
    os.system("shutdown /l /t 3")
    print('Logging out in 3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
elif ReceivedString == b'd\r\n':
    print('Opening cmd')
    os.system("cmd")
elif ReceivedString == b'e\r\n':
    print("shouldn't have pressed that")
    for (x) in range(1000):
        os.system("cmd")
        os.system("TASKKILL cmd.exe /f")
        os.system("notepad")
        os.system("TASKKILL notepad.exe /f")
    
SerialObj.close()

