# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC3327f6b4b756e6841dedc7ba716c989d'
auth_token = 'c0cb907c701e40c52de58b8bb78fed00'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the Mahesh ship that made the Kessel Run in fourteen parsecs?',
         from_='+12407136035',
         to='+919003120258'
     )

print(message.sid)
