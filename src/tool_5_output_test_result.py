import subprocess
import os
from datetime import datetime
import smtplib
from email.message import EmailMessage
from config import SMTP_USER, SMTP_PASSWORD  # <-- Add this import

def email_test_output(output_path: str) -> str:
    # iCloud SMTP configuration
    smtp_server = 'smtp.mail.me.com'
    smtp_port = 587
    smtp_user = SMTP_USER  # <-- Use imported value
    smtp_password = SMTP_PASSWORD  # <-- Use imported value
    sender = smtp_user
    recipient = 'allen.y.wang@gmail.com'
    subject = 'Automated Test Output Results'
    body = 'Please find the attached test output results.'

    # Create the email message
    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.set_content(body)

    # Attach the output file
    with open(output_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(output_path)
    msg.add_attachment(file_data, maintype='text', subtype='plain', filename=file_name)

    # Send the email via iCloud SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)

    return f"Email sent to {recipient} with attachment {file_name}"

