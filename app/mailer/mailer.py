import smtplib
from email.message import EmailMessage


class Mailer:
    """
    Wrapper around the EmailMessage implementation.
    """

    def __init__(self, email_address: str, password: str) -> None:
        """
        Configure the sender/receipient e-mail address, and password.
        """
        self.email_address: str = email_address
        self.password: str = password

    def compose_email(self, recipient: str, file: str):
        """
        Build the e-mail containing the converted mp3 data.
        """
        msg = EmailMessage()
        msg['Subject'] = 'Your Converted Video'
        msg['From'] = self.email_address
        msg['To'] = recipient

        msg.set_content("The .mp3 file is attached to this e-mail.")

        with open(file, 'rb') as content_file:
            content = content_file.read()
            msg.add_attachment(content, maintype='audio', subtype='mpeg', filename=file)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.email_address, self.password)
            smtp.send_message(msg)
