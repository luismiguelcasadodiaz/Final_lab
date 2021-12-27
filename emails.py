import smtplib
from email.message import EmailMessage
import mimetypes
import os
def generate_mail(sender, receiver, subject, body, path_to_attach,filename=None ):
    m=EmailMessage()
    m["From"]=sender
    m["To"]=receiver
    m["Subject"]=subject 
    m.set_content(body)
    if filename != None:
        mime_type, _ = mimetypes.guess_type(path_to_attach)
        m_type, m_subtype = mime_type.split("/",1)
        with open(path_to_attach, 'rb') as attach:
            m.add_attachment(attach.read(),
                maintype = m_type, 
                subtype = m_subtype, 
                filename = path_to_attach)
    return m

def send_mail(msg):
    server = smtplib.SMTP('localhost')
    server.set_debuglevel(1)
    server.send_mail(msg)
    server.quit()
    pass

