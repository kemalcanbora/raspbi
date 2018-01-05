import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
import os


def send_email(gmail_user,gmail_pwd, send_to, subject, text,path):
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = (send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))


    part = MIMEBase('application', "octet-stream")
    with open(path, 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(path)))
    msg.attach(part)
    try:
        print("buraya geldi burası mail kısmı-3")
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo()
        server_ssl.login(gmail_user, gmail_pwd)
        server_ssl.sendmail(gmail_user, send_to, msg.as_string())
        server_ssl.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail"),

