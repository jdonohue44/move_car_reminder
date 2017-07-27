# This script will run the day before the first Friday of every month, reminding user to move their car for street cleaning.
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

source = 'espressmorningnews@gmail.com'
dest = 'jared.donohue@gmail.com'

message = MIMEMultipart()
message['From'] = source
message['To'] = dest
message['Subject'] = 'STREET CLEANING TOMORROW'

body = MIMEText("Street cleaning occurs on Brookline street the first Friday of every month.", 'plain')
message.attach(body)

try:
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()
    smtp_server.login(source, '5638JabroniStreet**')
except Exception:
    print("ERROR connecting to email server")

# send email
try:
   smtp_server.sendmail(source, dest, message.as_string())
   smtp_server.quit()
except smtplib.SMTPException:
   print("Error: unable to send email")
