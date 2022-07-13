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

    def compose_email(self, item: str, recipient: str):
        """
        Build the e-mail containing the converted mp3 data.
        """
        EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS') or 'nil'
        EMAIL_PASSWORD = os.environ.get('EMAIL_PASS') or 'nil'

        #contacts = ['YourAddress@gmail.com', 'test@example.com']

        msg = EmailMessage()
        msg['Subject'] = 'Your Converted Video'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient

        #msg.set_content('This is a plain text email')

        msg.add_alternative("""\
        <!DOCTYPE html>
        <html>
            <body>
                <h1 style="color:SlateGray;">MP3 Conversion</h1>
            </body>
        </html>
        """, subtype='html')


        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
