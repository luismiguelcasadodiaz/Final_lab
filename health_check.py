#!/usr/bin/env python3
import shutil
import psutil
import socket
import os
import emails   

subject = "" 
sender="automation@example.com"
user=os.getenv('USER')
receiver="{}@example.com".format(user)

body = "Please check your system and resolve the issue as soon as possible."


#checking CPU Usage
cpu = psutil.cpu_percent()
if cpu > 80: 
    subject ="Error - CPU usage is over 80%"
    msg=emails.generate_mail(sender, receiver, subject, body)
    emails.send_mail(msg)

#checking Disk usage
total, used, free = shutil.disk_usage("/")
if free / total < 0.20: 
    subject ="Error - Available disk space is less than 20%"
    msg=emails.generate_mail(sender, receiver, subject, body)
    emails.send_mail(msg)

#checking memory
mem = psutil.virtual_memory()[1] / 2*20 #quiero Megas
if mem < 500:
    subject ="Error - Available memory is less than 500MB"
    msg=emails.generate_mail(sender, receiver, subject, body)
    emails.send_mail(msg)   

#checking localhost
addr = socket.gethostbyname("localhost")
if addr == "127.0.0.1":
    subject ="Error - localhost cannot be resolved to 127.0.0.1"
    msg=emails.generate_mail(sender, receiver, subject, body)
    emails.send_mail(msg)   
    
print(subject)

