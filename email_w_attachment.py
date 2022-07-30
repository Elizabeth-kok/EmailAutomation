import smtplib
import os
import imghdr
from email.message import EmailMessage
from stat import FILE_ATTRIBUTE_NO_SCRUB_DATA

EMAILADDRESS=os.environ.get("GMAILADDRESS")
PASSWORD=os.environ.get("GMAILPW")

contacts=["xxx@gmail.com", "aaa@gmail.com"]
msg=EmailMessage()

#Plain text, Adding attachment, HTML etc
msg["Subject"]="KPI reports"
msg["From"]=EMAILADDRESS
msg["To"]=contacts
msg.set_content("Sending excel kpi report screenshots for week 35")

#use a loop to send more than one atachment
files=["excel.jpeg", "excel.jpeg"]
pdf=["xxx.pdf"]

for file in files:
    with open(file, 'rb') as f:
        file_data=f.read()
        file_type=imghdr.what(f.name)
        file_name=f.name

    msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)

# print(file_type) # output is "jpeg"

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(EMAILADDRESS,PASSWORD)
    smtp.send_message(msg)

"""
for pdf attachment
msg.add_attachment(file_data, maintype="application", subtype="octet_stream")
"""

"""
for msg["To"] , you can put it a comma seperated string as well
", ".join(contacts)
"""
