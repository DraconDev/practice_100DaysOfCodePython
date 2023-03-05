import json

from twilio.rest import Client


def send_sms(text_to_send):
    with open('../../../_Login/_API/twilo.txt') as f:
        user_info = json.load(f)
        account_sid = user_info["SID"]
        auth_token = user_info["AUTH"]

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to='+447486872861', body=text_to_send,  from_='+15674093256'
    )

    print(message.sid)


# send_sms()
