#!/usr/bin/env python3
import requests
import os
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attach, title, paragraph):
    styles=getSampleStyleSheet()
    r=SimpleDocTemplate(attach)
    r_title=Paragraph(title,styles["h1"])
    r_info=Paragraph(paragraph)
    r.build([r_title, r_info])

