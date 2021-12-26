import smtplib
from email import EmailMessage
import mimetypes
def generate_mail(sender, receiver, subject, body, path_to_attach ):
    m=EmailMessage()
    m["From"]=sender
    m["To"]=receiver
    m["Subject"]=subject 
    m.set.content(body)
    mime_type, _ mimetypes.guess_type(path_to_attach)
    m_type, m_subtype = mime_type.split("/",1)
    with open(path_to_attach, 'rb') as attach:
        m.add_attachement(attach,read(),
                maintype = m_type, 
                subtype = m_subtype, 
                filename = path_to_attach)
    return m

def send_mail():
    pass
