import smtplib
from email.message import EmailMessage
import os, dotenv

dotenv.load_dotenv()

class Emailer:
    """Contains functions for composing and sending emails."""


    def __init__(self, contents: dict[str, str | float]):
        self.contents = contents

    
    def send(self):
        # Create a text/plain message
        msg = EmailMessage()
        msg.set_content(
            f"Total Portfolio Worth: ${round(self.contents.get('sum_of_assets'), 2)} USD\n"
            f"Daily % Increase: {round(self.contents.get('percent_increase') * 100, 2)}%\n"
            f"Daily $ Increase: ${round(self.contents.get('dollar_increase'), 2)} USD\n"
            f"Daily Best Performer: {self.contents.get('best_performer')}\n"
        )

        # Gather sender's email & password and recipient's email
        sender = os.getenv('SENDER_EMAIL')
        password = os.getenv('SENDER_PASSWORD')
        recipient = os.getenv('RECEIVER_EMAIL')

        # sender == the sender's email address
        # recipient == the recipient's email address
        msg['Subject'] = "Daily Portfolio Report"
        msg['From'] = sender
        msg['To'] = recipient

        # Send the message via Yahoo Mail SMTP
        with smtplib.SMTP('smtp.mail.yahoo.com', 587) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(sender, password)  # App password only
            server.send_message(msg)
