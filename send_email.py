import smtplib
import ssl
from email.message import EmailMessage
import os

def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path=None):
    try:
        # Create EmailMessage object
        msg = EmailMessage()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.set_content(body)

        # Attach file if provided
        if attachment_path:
            if os.path.exists(attachment_path):
                with open(attachment_path, "rb") as file:
                    file_data = file.read()
                    file_name = os.path.basename(attachment_path)
                    msg.add_attachment(file_data, maintype="application",
                                       subtype="octet-stream", filename=file_name)
                print(f"[+] Attached file: {file_name}")
            else:
                print(f"[!] Attachment not found: {attachment_path}")

        
        context = ssl.create_default_context()
        print("[+] Connecting to Gmail server...")

      
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, sender_password)
            print("[+] Login successful!")
            server.send_message(msg)
            print("[✔] Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("[X] Authentication failed! Check your email password or enable App Password.")
    except Exception as e:
        print(f"[X] Error occurred: {e}")

if __name__ == "__main__":
    print("=== Automated Email Sender ===")

    sender_email = input("Enter your Gmail ID: ")
    sender_password = input("Enter your App Password: ")
    receiver_email = input("Enter receiver email: ")
    subject = input("Enter Subject: ")
    body = input("Enter Message Body: ")

    attach = input("Do you want to attach a file? (yes/no): ").lower()

    attachment_path = None
    if attach == "yes":
        attachment_path = input("Enter file path: ")

    send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path)
