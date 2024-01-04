import os
from twilio.rest import Client  # Importing client from Twilio Module

#I have a Trial Account on Twilio!!

def call(FromNumber, ToNumber):
    account_sid = os.environ["AccSID"]  # AccountSID and Auth Token Can BE Aloted To Ur Twilio Account
    auth_token = os.environ["AuthTok"]      # Find your Account SID and Auth Token at https://www.twilio.com/console

    client = Client(account_sid, auth_token)  # Initialize the client Object

    # Defining Call Instance With Followeing Parametres
    call = client.calls.create(
        method="GET",
        send_digits="1234#", # Send the Digits Which Is Decoded To Determine The Pause duration after Call IS Connected
        url="http://demo.twilio.com/docs/voice.xml",  # Url Of Caller API Website
        to=ToNumber,  # Enter The Number From Which You Wanna Call
        from_=FromNumber,  # Enter The To Which You Wanna Connect The Call
    )
    print(call.sid) #Prints The Stauts Of The Request We Made To Call The "ToNumber"  
   
if __name__ == "__main__":
    
    From = int(input("Enter The Number From Which You Wanna Call: \n"))
    To = int(input("Enter The To Which You Wanna Connect the Call: \n"))
    
    call(From, To)  #Function Calling By Given Numbers From Input


#For Any Information Visit https://www.twilio.com