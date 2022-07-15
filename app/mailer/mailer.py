import os
import smtplib
from email.message import EmailMessage


class Mailer:

    def __init__(self) -> None:
        """
        Configure the sender/receipient e-mail address, and password.
        """
        self.email_address: str = os.environ.get('EMAIL_ADDRESS') or 'nil'
        self.password: str = os.environ.get('EMAIL_PASS') or 'nil'

    def compose_email(self, recipient: str, item: str):
        """
        Build the e-mail containing the converted mp3 data.
        """
        EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS') or 'nil'
        EMAIL_PASSWORD = os.environ.get('EMAIL_PASS') or 'nil'

        msg = EmailMessage()
        msg['Subject'] = 'Your Converted Video'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient

        msg.set_content("The .mp3 file is attached to this e-mail.")

        with open(item, 'rb') as content_file:
            content = content_file.read()
            msg.add_attachment(content, maintype='audio', subtype='mpeg', filename=item)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)


x = Mailer()
x.compose_email("johann.suarez92@gmail.com", "song.mp3")
