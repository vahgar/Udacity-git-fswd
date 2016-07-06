from twilio.rest import TwilioRestClient

account_sid = "ACf3c0e3978a503e38318822axxxxx39d40d" # Your Account SID from www.twilio.com/console
auth_token  = "8c611916de771d3b5a47caxxxxx2734f"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hey Navdeep,Want to win free trip to Manchester United's ? Like this is real hahahhahah",
    to="+918053500445", # Replace with your phone number
    from_="+12566670995") # Replace with your Twilio number

print(message.sid)
