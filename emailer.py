import smtplib
from email.message import EmailMessage
from file_handler import FileHandler as FH

class Emailer:
    """Contains functions for composing and sending emails."""


    def __init__(self, contents: dict[str, str | float]):
        self.contents = contents

    
    def send(self):
        # Create a text/plain message
        msg = EmailMessage()
        msg.set_content(
            f"Total Portfolio Worth: {self.contents.get('sum_of_assets')}\n"
            f"Daily % Increase: {self.contents.get('percent_increase')}\n"
            f"Daily $ Increase: {self.contents.get('dollar_increase')}\n"
            f"Daily Best Performer: {self.contents.get('best_performer')}\n"
        )

        # Gather sender and recipient
        json_config = FH.read_json("config.json")
        sender = json_config.get("sender_email")
        password = json_config.get("sender_password")
        recipient = json_config.get("receiver_email")

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
            server.quit()
