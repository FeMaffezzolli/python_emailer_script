# send_attachment.py
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib
# create message object instance
msg = MIMEMultipart()


# setup the parameters of the message
password = "email_password"
msg['From'] = "email_address"
msg['To'] = "email_address"
msg['Subject'] = "email_subject"

# attach image to message body
with open('image.jpg', 'rb') as img:
    msg.attach(MIMEImage(img.read()))

# create server
server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()

# Login Credentials for sending the mail
server.login(msg['From'], password)

# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print ("successfully sent email to %s:" % (msg['To']))