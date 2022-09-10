#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Mario Burgos
# Tutorial: https://github.com/tomitokko/20-python-projects
# Youtube: https://youtu.be/pdy3nh1tn6I
# Created Date: Fri Sep  9 03:18:01 PM PDT 2022
# version ='1.0'

## TODO: Import crecentials from ENV Variables:
## Environmet variables preferred: https://medium.com/geekculture/how-to-protect-your-credentials-using-environment-variables-with-python-25e6cb4d135c

## credentials.py
## app_password = "<application_password>"

from email.message import EmailMessage
from credentials import app_password # Import from credentials.py
import ssl
import smtplib


sender = '<myemail@emailhost.com>'
password = app_password
receiver = input("Send email to: ")
subject = input("Subject: ")
body = input("Message to send: ")

email_message = EmailMessage()
email_message['From'] = sender
email_message['To'] = receiver
email_message['Subject'] = f"Sent with Python: {subject}" # Add a subject prefix
email_message.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    try:
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, email_message.as_string())
        print(f"Message sent...\n\n{email_message}")
    except smtplib.SMTPAuthenticationError as error:
        print("Error: Username and Password not accepted.")
