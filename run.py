# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 10:29:48 2021

@author: LuisMiguel
"""

#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/fruits/"
my_dir = os.path.abspath(".")
fruits_dir = os.path.join(my_dir, "supplier-data/descriptions")
images_dir = os.path.join(my_dir, "suppler-data/images")
for f in os.listdir(fruits_dir):
    if f.endswith(".txt"):
        imagen_file = os.path.join(fruits_dir, f)
        with open(imagen_file, 'r') as opened:
            c_r = {}
            c_r["name"]= opened.readline()[:-1]
            c_r["weight"]=int(opened.readline()[:-1].replace("lbs",""))
            c_r["description"]=opened.readline()[:-1]
            c_r["image_name"]=  f.replace(".txt",".jpeg"))
            print(c_r)
            r = requests.post(url, json=c_r)
