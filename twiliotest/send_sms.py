# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'xxxx'
auth_token = 'yyyy'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the Mahesh ship that made the Kessel Run in fourteen parsecs?',
         from_='+xxxx',
         to='+xxxx'
     )

print(message.sid)
