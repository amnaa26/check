import aiomail
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASS")

smtp_url = f"smtp://{email}:{password}@smtp.gmail.com:587"

# Function to send email
async def send_email(recipient: str, subject: str, body: str):
    # Create email message
    message = aiomail.Message(
        subject=subject,
        recipients=[recipient],
        body=body,  # Use `html=body` if you're sending HTML content
    )
    
    try:
        # Connect to the SMTP server and send email
        async with aiomail.from_url(smtp_url) as client:
            await client.send(message)
            print(f"Email sent to {recipient}!")
    except Exception as e:
        print(f"Error sending email: {e}")

