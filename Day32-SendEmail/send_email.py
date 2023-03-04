# import datetime as dt
import datetime as dt
import smtplib
import ssl
from email.message import EmailMessage

from random_quote import rand_quote
from user_info import User

# * Set specific time
time = dt.datetime.now().minute+1

# * Get User
user = User()

# * Define email sender and receiver
email_sender = user.email
email_password = user.code
email_receiver = user.email

# * Set the subject and body of the email
subject = 'Happy birthday'
body = """
Test
"""

body = rand_quote()

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# * Add SSL (layer of security)
context = ssl.create_default_context()

# * Log in and send the email


def send_email():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


# * Send email at X time
while True:
    if time == dt.datetime.now().minute:
        print('sent')
        send_email()
        break
