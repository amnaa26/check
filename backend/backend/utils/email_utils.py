import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def send_otp_email(to_email, otp):
    email_sender = os.getenv("EMAIL_USER")
    email_password = os.getenv("EMAIL_PASS")

    msg = EmailMessage()
    msg['Subject'] = 'Your OTP Verification Code'
    msg['From'] = email_sender
    msg['To'] = to_email
    msg.set_content(f"Your OTP code is: {otp}")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_sender, email_password)
        smtp.send_message(msg)
