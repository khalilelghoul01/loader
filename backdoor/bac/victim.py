#victim
import socket, os
connected=False
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while not connected:
    try:
        yourip="192.168.1.43" #your ip address or DNS
        s.connect((yourip, 6666))
        connected=True
        print(addr, "has connected to the server successfully")
    except:
        print("check adress")
        pass
while True:
    comm=s.recv(2000)
    comm=comm.decode()
    if comm == "hi1":
        print("hi")
    else:
        print('off')
