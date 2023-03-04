import datetime as dt
import smtplib
import ssl
from email.message import EmailMessage

import pandas
from random_quote import rand_quote
from user_info import User

data = pandas.read_csv("./data/birthdays.csv")
# * Strip extra whitespace
str_cols = data.select_dtypes(include=['object']).columns
data[str_cols] = data[str_cols].apply(lambda x: x.str.strip())
data

print(data)

with open('./data/letter_templates/letter_1.txt') as f:
    letter = f.read()
    letter = letter.replace('[NAME]', data.at[0, 'name'])

print(letter)

# * Set specific time
time = dt.datetime.now().minute+1

# * Get User
user = User()

# * Define email sender and receiver
email_sender = data.at[0, 'email']
email_password = user.code
email_receiver = data.at[0, 'email']

# * Set the subject and body of the email
subject = 'Happy birthday'
body = """
Test
"""

# body = rand_quote()
body = letter

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
