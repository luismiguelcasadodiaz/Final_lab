#!/usr/bin/env python3
import shutil
import psutil
import socket    

cpu = psutil.cpu_percent()

if cpu > 80:
    print("mucho uso de cpu")

total, used, free = shutil.disk_usage("/")
if free / total < 0.20:
    print("es menor del 20%")
    
mem = psutil.virtual_memory()[1] / 2*20 #quiero Megas

if mem < 500:
    print("Poca memoria")    
    

addr = socket.gethostbyname("localhost")
if addr == "127.0.0.1":
    print(f"Your ip is {addr}")