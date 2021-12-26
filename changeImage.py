#!/usr/bin/env python3
import os
from PIL import Image as im
my_dir = os.path.abspath(".")

original_dir = os.path.join(my_dir, "supplier-data/images")
dest_dir = os.path.join(my_dir,"supplier-data/images")

for f in os.listdir(original_dir):
    if f.endswith(".tiff"):
        image_file = os.path.join(original_dir, f)
        rot_f = f.replace("tiff","jpeg")
        r_image_file = os.path.join(dest_dir, rot_f)
        im_in = im.open(image_file)
        rgb_im = im_in.convert("RGB")
        scaled_im = rgb_im.resize((600,400))
        scaled_im.save(r_image_file,format="JPEG")

