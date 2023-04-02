import os
from twilio.rest import Client

account_sid = "AC5e91742dd982da7003b3f1d730b54550"
auth_token = "e0d3b2a8480c6396eaeee67495b1b498"
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
