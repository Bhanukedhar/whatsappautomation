from twilio.rest import Client

account_sid = 'AUTH_SID'
auth_token = 'AUTH_KEY'
client = Client(account_sid, auth_token)


def alert():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hello World',
        to='whatsapp:+919999999999'
    )

    print(message.sid)
