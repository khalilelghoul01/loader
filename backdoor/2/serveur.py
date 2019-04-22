import socket, subprocess as sp, sys

host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
conn, addr = s.accept()

print ("[+] Connection etablie avec l hote : %s" %(str(addr[0])))

while 1:
    command = input("#>")
    if command == "" :continue

    conn.send(command)
    result = conn.recv(1024)
    total_size = long(result[:16])
    result = result[16:]
       
