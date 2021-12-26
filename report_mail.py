#!/usr/bin/env python3

import os
from datetime import date
import reports

def report_body():
    text=""
    my_dir = os.path.abspath(".")
    fruits_dir = os.path.join(my_dir, "supplier-data/descriptions")
    for f in os.listdir(fruits_dir):
        if f.endswith(".txt"):
            file_path=os.path.join(fruits_dir, f)
            with open(file_path,'r') as opened:
                c_r={}
                c_r["name"]=opened.readline()[:-1]
                c_r["weigth"]=opened.readline()[:-1]
                for k,v in c_r.items():
                    text = text + k + ": " + v + "\n"
                text += "\n"
    return text
def report_title():
    today = date.today()
    return "Processed Update on " + today.strftime("%d/%m/%y") 
if __name__ == "__main__":
    parafo = report_body()
    titulo = report_title()
    print(titulo)
    print(parafo)
    report_path = "/tmp/processed.pdf"
    reports.generate_report(report_path,titulo, parafo)

