import smtplib
from email.mime.text import MIMEText

messages = [
    {
        "subject": "VPN Credentials Update",
        "body": "Hi, here's the updated VPN config:\nUsername: hshield.it\nPassword: P@ssw0rd123\nPlease do not share this externally.",
    },
    {
        "subject": "Finance Q1 Report",
        "body": "Attached is the Q1 payroll report. Confidential data for internal review only.\n- CFO",
    },
    {
        "subject": "Security Alert",
        "body": "We’ve noticed multiple failed login attempts. Please change your password immediately using the following link:\nhttp://intranet.hackshield/reset",
    }
]

for msg in messages:
    email = MIMEText(msg["body"])
    email['Subject'] = msg["subject"]
    email['From'] = 'it-support@hackshield.com'
    email['To'] = 'employee@hackshield.com'

    with smtplib.SMTP('localhost', 1025) as smtp:
        smtp.send_message(email)

print("✓ Sent sample messages to Mailpit inbox.")
