# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 10:04:53 2021

@author: LuisMiguel
"""

#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
my_dir = os.path.abspath(".")
images_dir = os.path.join(my_dir, "supplier-data/images")
for f in os.listdir(images_dir):
    if f.endswith(".jpeg"):
        imagen_file = os.path.join(images_dir, f)
        with open(imagen_file, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
