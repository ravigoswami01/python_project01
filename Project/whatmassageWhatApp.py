from twilio.rest import Client
from datetime import datetime, timedelta
import time
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
client = Client(account_sid, auth_token)


def send_message(phone_number, message_body):
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=message_body,
        to=f'whatsapp:{6394732716}'
    )
    print(f'Message sent with SID: {message.sid}')  


# take user input

Name = input("Enter your name: ")
Phone_number = input("Enter your phone number (with country code): ")
massage_body = input("Enter your message: ")

# date and time for scheduling
schedule_time = input("Enter the date and time to send the message (YYYY-MM-DD HH:MM): ")
schedule_time = datetime.strptime(schedule_time, "%Y-%m-%d %H:%M")

# date and time handle for client

send_time = schedule_time - datetime.now()
if send_time.total_seconds() > 0:
    print(f"Message scheduled to be sent at {schedule_time}")
    time.sleep(send_time.total_seconds())
    send_message(Phone_number, massage_body)
else:
    print("Scheduled time must be in the future.")

time.sleep(5)  # Wait for 5 seconds before ending the program