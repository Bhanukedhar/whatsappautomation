from twilio.rest import Client

account_sid = 'AUTH_SID'
auth_token = 'AUTH_KEY'
client = Client(account_sid, auth_token)


def alert():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hi Bhanu Put your phone away and study',
        to='whatsapp:+919059461340'
    )

    print(message.sid)
