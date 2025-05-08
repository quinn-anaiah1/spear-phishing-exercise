import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

messages = [
    {
        "subject": "VPN Credentials Update",
        "body": "Hi, here's the updated VPN config:\nUsername: hshield.it\nPassword: P@ssw0rd123\nPlease do not share this externally.",
        "sender": "it@hackshield.com",
    },
    
    {
        "subject": "Finance Q1 Report",
        "body": "Attached is the Q1 payroll report. Confidential data for internal review only.\n- CFO",
        "sender": "hr@hackshield",
        "attachment": "mailpit/q1_finance_report.csv",
    },
    {
        "sender": "hiring@hackshield",
        "subject":"Re: Salary Ranges and Offer Notes",
        "body": "Following up on our earlier chat — let’s move forward with the Security Analyst role at $74–80k depending on certs.Let’s also avoid mentioning the signing bonus until we confirm budget approval. We’ll reassess if candidate negotiates." , 
    },
    {  "sender": "decrypt@hackshield.com",
        "body": "5ad153689151b83f682f2df21295aff2",
        "subject": "Super Secret ",
    },
    {   "sender": "it@hackshield",
        "subject": "Security Alert",
        "body": "We’ve noticed multiple failed login attempts. Please change your password immediately using the following link:\nhttp://intranet.hackshield/reset",
        
    }, {
        "sender": "leadership@hackshield.com",
        "subject":" Q2 All-Hands Reminder",
        "body": "Just a reminder that our Q2 All-Hands meeting is scheduled for Friday at 3 PM. Please be on time — we’ll be highlighting performance metrics, project updates, and department goals. Snacks in the break room after!" , 
    }
    , {
        "sender": "it@hackshield.com",
        "subject":"New Cypersecurity Training Deadlines",
        "body": "The deadline to complete the annual cybersecurity training has been extended to May 15th. Failure to complete it may result in temporary access restrictions. Please contact IT with any issues accessing the training portal." , 
    }, {
        "sender": "hiring@hackshield.com",
        "subject":"[CONFIDENTIAL] Interview Questions: Security Analyst Role",
        "body": "Attached youll find the interview questions for the upcoming position. For securty reasons the file has been encrypted. Per usual the decryption key  will be sent separately",
        "attachment": "mailpit/interview_file_ecb.enc",
    }
    
]

for msg in messages:
    if "attachment" in msg:
        # Use MIMEMultipart for emails with attachments
        email = MIMEMultipart()
        email.attach(MIMEText(msg["body"], 'plain'))

        filename = msg["attachment"]

        if os.path.isfile(filename):
            # Attach the encrypted (or binary) file
            with open(filename, "rb") as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(f.read())
                encoders.encode_base64(part)  # Encode to base64 for safe transport over SMTP
                part.add_header('Content-Disposition', f'attachment; filename="{filename}"')
                email.attach(part)
        else:
            print(f"⚠ File not found: {filename}, skipping email.")
            continue  # Skip sending if the file is missing
    else:
        # Plain text-only email
        email = MIMEMultipart()  # Still use MIMEMultipart for consistency
        email.attach(MIMEText(msg["body"], 'plain'))
        
    email['Subject'] = msg["subject"]
    email['From'] = msg["sender"]
    email['To'] = 'employee@hackshield.com'

    with smtplib.SMTP('localhost', 1125) as smtp:
        smtp.send_message(email)

print("✓ Sent sample messages to Mailpit inbox.")
