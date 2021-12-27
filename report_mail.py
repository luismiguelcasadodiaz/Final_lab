#!/usr/bin/env python3

import os
from datetime import date
import reports
import emails

def report_body():
    text="<br/><br/>"
    c_r={}
    my_dir = os.path.abspath(".")
    fruits_dir = os.path.join(my_dir, "supplier-data/descriptions")
    for f in os.listdir(fruits_dir):
        if f.endswith(".txt"):
            file_path=os.path.join(fruits_dir, f)
            with open(file_path,'r') as opened:
                #c_r={}
                #c_r["name"]=opened.readline()[:-1]
                #c_r["weigth"]=opened.readline()[:-1]
                #for k,v in c_r.items():
                #    text = text + k + ": " + v + "<br/>"
                #text += "<br/>"
                name = opened.readline()[:-1]
                weigth = opened.readline()[:-1]
                if name not in c_r:
                    c_r.setdefault(name, weigth)
                else:
                    c_r[name]= weigth
    for k,v in sorted(c_r.items(), key=lambda x:x[0]):
        text = text + "name: " + k + "<br/>"
        text = text + "weigth: " + v + "<br/><br/>"

    return text
def report_title():
    today = date.today()
    return "Processed Update on " + today.strftime("%B %d, %Y") 
if __name__ == "__main__":
    parafo = report_body()
    titulo = report_title()
    report_path = "/tmp/processed.pdf"
    reports.generate_report(report_path,titulo, parafo)
    sender="automation@example.com"
    user=os.getenv('USER')
    receiver="{}@example.com".format(user)
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website succesfully.A detailed list is attached to this email"
    filename="processed.pdf"
    msg=emails.generate_mail(sender, receiver, subject, body, report_path, filename)
    emails.send_mail(msg)


