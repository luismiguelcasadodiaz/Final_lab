#!/usr/bin/env python3
import requests
import os
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attach, title, thetext):
    contenido=[]
    bline=Spacer(1,20)
    styles=getSampleStyleSheet()
    r=SimpleDocTemplate(attach)
    r_title=Paragraph(title,styles["h1"])
    contenido.append(r_title)
    contenido.append(bline)
    count = 0
    for name, weight in thetext:
        r_info=Paragraph("name: "+name+"<br />", styles["BodyText"])
        contenido.append(r_info)
        r_info=Paragraph("weight: "+weight+"<br />", styles["BodyText"])
        contenido.append(r_info)
        contenido.append(bline)
    r.build(contenido)
