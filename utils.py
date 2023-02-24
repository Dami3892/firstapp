import os
from twilio.rest import Client

account_sid = 'AC080c1e86399e699a8773ce3d79d43d21'
auth_token = '51e23f147d868ebcf0478fd6ce020a96'
client = Client(account_sid,auth_token)

def send_sms (user_code,phone_number):

     message = client.messages.create(
                                 body=f'Hi!your user and verification code is (user)',
                                 from_=+17125457082,
                                 to=f'{phone_number}'
                          )

     print(message.sid)