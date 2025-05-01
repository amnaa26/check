import aiosmtplib
from email.message import EmailMessage
import os

email_sender = os.getenv("EMAIL_USER")
email_password = os.getenv("EMAIL_PASS")

async def send_email(to_email: str, subject: str, body: str):
    # Set up the email content
    message = EmailMessage()
    message["From"] = email_sender # Replace with your email address
    message["To"] = to_email
    message["Subject"] = subject
    message.set_content(body)

    # Gmail SMTP settings
    smtp_host = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = email_sender  # Your Gmail address
    smtp_password = email_password  # Use app-specific password for better security

    # Send the email
    try:
        await aiosmtplib.send(
            message,
            hostname=smtp_host,
            port=smtp_port,
            start_tls=True,
            username=smtp_user,
            password=smtp_password
        )
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

