import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Update these settings with the provided SMTP configuration
smtp_server = "premium186.web-hosting.com"
smtp_port = 465  # SSL port for SMTP
smtp_username = "payments@intaree.com"
smtp_password = "RIYAD2580"  # Replace with the actual password

# Sender
from_email = smtp_username

# Function to send email
def send_email(to_email, subject, html_content):
    # Create message
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = from_email
    message["To"] = to_email

    # Attach HTML content to MIMEMultipart message
    part = MIMEText(html_content, "html")
    message.attach(part)

    # Send email using SSL
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:  # Note the use of SMTP_SSL instead of SMTP
            server.login(smtp_username, smtp_password)
            server.sendmail(from_email, to_email, message.as_string())
            print(f"Email sent successfully to {to_email}!")
    except Exception as e:
        print(f"Error sending to {to_email}: {e}")

# Read the content of 'letter.html' for the email body
with open('letter.html', 'r') as file:
    html_content = file.read()

# Ask for the email subject
subject = input("Enter the email subject: ")

# Read email addresses from file and send emails
with open('email_list.txt', 'r') as file:
    emails = [email.strip() for email in file.readlines()]  # Remove any leading/trailing whitespace

# Ask how many times to send the email
try:
    num_times = int(input("Enter the number of times each email should be sent: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

for email in emails:
    for _ in range(num_times):
        send_email(email, subject, html_content)
