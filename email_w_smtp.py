import smtplib
import os

EMAILADDRESS=os.environ.get("GMAILADDRESS")
PASSWORD=os.environ.get("GMAILPW")

# print(EMAILADDRESS,PASSWORD)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAILADDRESS,PASSWORD)

    subject="KPI Report week 22"
    body="Sending weekly kpi report"

    msg=f"Subject:{subject}\n\n{body}"

    smtp.sendmail(EMAILADDRESS, "elizabethkok_97@hotmail.com", msg)
