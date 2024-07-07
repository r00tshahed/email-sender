import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_email():
    try:
        # Use environment variables for email and password
        email_address = ''
        email_password = ''
        
        # Set up the server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        
        # Log in to the server
        server.login(email_address, email_password)
        
        # Create the email content
        subject = "hello"
        body = "hi"
        
        # Set up the MIME
        message = MIMEMultipart()
        message['From'] = email_address
        message['To'] = '',
        message['Subject'] = subject
        
        # Attach the body with the msg instance
        message.attach(MIMEText(body, 'plain'))
        
        # Send the email
        server.sendmail(email_address, 'reciver email', message.as_string())
        
        print("Email has been successfully sent")
        
    except Exception as e:
        print(f"Failed to send email: {e}")
    
    finally:
        # Terminate the SMTP session and close the connection
        server.quit()

if __name__ == "__main__":
    send_email()
