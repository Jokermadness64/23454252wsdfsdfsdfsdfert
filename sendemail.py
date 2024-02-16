import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define SMTP configurations
smtp_configurations = [
    {"smtp_username": "payments@intaree.com"},
    {"smtp_username": "refund.gov@intaree.com"},
    {"smtp_username": "paymants@intaree.com"},
]

smtp_server = "premium186.web-hosting.com"
smtp_port = 465
smtp_password = "RIYAD2580"  # Assuming the password is the same for all configurations

# Function to send email using a specific SMTP configuration
def send_email(smtp_username, from_email, to_email, subject, html_content):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = from_email
    message["To"] = to_email

    part = MIMEText(html_content, "html")
    message.attach(part)

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(smtp_username, smtp_password)
            server.sendmail(from_email, to_email, message.as_string())
            print(f"Email sent successfully to {to_email} using {smtp_username}!")
    except Exception as e:
        print(f"Error sending to {to_email} using {smtp_username}: {e}")

# Read email content from file
with open('letter.html', 'r') as file:
    html_content = file.read()

# Prompt for email subject
subject = input("Enter the email subject: ")

# Read email addresses from file
with open('email_list.txt', 'r') as file:
    emails = [email.strip() for email in file.readlines()]

# Prompt for the number of times each email should be sent
try:
    num_times = int(input("Enter the number of times each email should be sent: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

# Iterate through SMTP configurations and send emails
for smtp_config in smtp_configurations:
    smtp_username = smtp_config["smtp_username"]
    for email in emails:
        for _ in range(num_times):
            send_email(smtp_username, smtp_username, email, subject, html_content)

