#! python3

import credentials
from twilio.rest import Client

# Preset values:
accountSID = credentials.Twilio_accountSID
authToken = credentials.Twilio_authToken
myNumber = credentials.Twilio_myNumber

def sendSMS(to, body):
    client = Client(accountSID, authToken)
    client.api.account.messages.create(to=to, from_=myNumber, body=body)
