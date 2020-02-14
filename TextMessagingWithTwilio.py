from twilio.rest import Client
import time

## Program to send text reminder (every 'x' seconds) with personal message.

account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
client = Client(account_sid, auth_token)


def SendMessage(message,from_number,to_number):
    message = client.messages \
                .create(
                     body=message,
                     from_=from_number,
                     to=to_number
                 )
    print(message.sid)

def SendReminder(message,from_number,to_number):
    if type(to_number) is not str or type(from_number) is not str or type(message) is not str:
        raise TypeError("Argument needs to be a string.")
    SendMessage(message,from_number,to_number)

while True:
    time.sleep(10) # wait 10 seconds
    SendReminder('Your_Message_Here','YOUR_TRIAL_NUMBER','SEND_MESSAGE_TO_NUMBER') # Replace link here.