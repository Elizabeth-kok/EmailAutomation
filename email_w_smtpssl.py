import smtplib
import os
from email.message import EmailMessage

EMAILADDRESS=os.environ.get("GMAILADDRESS")
PASSWORD=os.environ.get("GMAILPW")

msg=EmailMessage()

#Plain text, Adding attachment, HTML etc
msg["Subject"]="KPI reports"
msg["From"]=EMAILADDRESS
msg["To"]="elizabethkok_97@hotmail.com"
msg.set_content("Sending reports for week 35")

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(EMAILADDRESS,PASSWORD)
    smtp.sendmail(msg)
