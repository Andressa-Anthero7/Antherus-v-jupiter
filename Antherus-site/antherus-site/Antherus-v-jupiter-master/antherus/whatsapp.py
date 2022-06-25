from twilio.rest import Client
import os

# Your Account SID from twilio.com/console
account_sid = "AC95d4a3b7262a74d20f1f52f3ac588308"
# Your Auth Token from twilio.com/console
auth_token = "6aeb03e7a4d4b4ef94b6ec57d833cff4"

client = Client(account_sid, auth_token)

# esse é o numero de teste da sandbox da Twilio
from_whatsapp_number = 'whatsapp:+14155238886'
# substitua esse número com o seu próprio número do Whatsapp
to_whatsapp_number = 'whatsapp:+5516993379492'

leads = ()

client.messages.create(body=from_whatsapp_number,
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
