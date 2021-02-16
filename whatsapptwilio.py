from twilio.rest import Client

account_sid = 'AC9b88b0850dd83e0cc32885a4510af590'
auth_token = '7c3a5613003065134757e7fb9eea846d'
client = Client(account_sid, auth_token)


def alert():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hi Bhanu Put your phone away and study',
        to='whatsapp:+919059461340'
    )

    print(message.sid)
