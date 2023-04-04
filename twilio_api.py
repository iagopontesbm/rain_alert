import os
from twilio.rest import Client

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
client = Client(account_sid, auth_token)

twilio_phone = "+14344258431"
my_phone = os.getenv("MY_PHONE")

def send_sms():
    message = client.messages \
        .create(
             body="Levar guarda chuva!☂️",
             from_=twilio_phone,
             to=my_phone
         )

    print(message.status)
