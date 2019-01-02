import smtplib
import email.message

email_content = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Document</title>
  </head>
  <body>
    <center>
      <h1> Hi there! </h1>
      <img src="image.jpg" alt="Imagem" srcset="" />
    </center>
  </body>
</html>
"""

msg = email.message.Message()

msg['From'] = 'email_address'
msg['Subject'] = 'Subject'

password = "email_password"
msg.add_header('Content-Type', 'text/html')
msg.set_payload(email_content)

s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()

# Login Credentials for sending the mail
s.login(msg['From'], password)

# You could read an excel/csv file using Pandas, for example
email_list = ['email_address', 'email_address', 'email_address']

for email in email_list:
    msg['To'] = email
    s.sendmail(msg['From'], [msg['To']], msg.as_string())

s.quit()
print ("successfully sent all emails from %s:" % (msg['From']))
