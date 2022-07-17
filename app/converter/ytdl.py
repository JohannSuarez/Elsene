import os
import subprocess

from typing import List
from app import ConversionQueue
from app import Configs
from app.mailer.mailer import Mailer
from subprocess import PIPE

class Converter:
    """
    A wrapper around a command line program (in this case youtube-dl)
    """

    def __init__(self):
        self.command: List[str] = []
        self.app: str = 'youtube-dl'
        self.flags_and_args: List[str] = [
            '--extract-audio',
            '--restrict-filenames',
            '-o ',
            '--audio-format',
            'mp3'
        ]

    @staticmethod
    def follow_up(proc: subprocess.Popen) -> None:
        """
        Manages the downloaded file, calling Mailer on it, and cleaning up afterwards.
        """

        # Run a debugging statement, print the directory this method is operating on.
        # From there, find the file.
        # Make a singleton that holds the filename of the video-to-be-downloaded, and the
        # email recipient information. This will give you persistence.
        proc.wait()

        # Find the file, send it to the recipient.
        mailer = Mailer(Configs.email_address, Configs.email_password)

        conversion_request: List = ConversionQueue.queue.pop(0)
        recipient_email = conversion_request[0]['recipient']
        file_salt: str = conversion_request[1]

        for item in os.listdir():
            if file_salt in item:
                mailer.compose_email(recipient_email, item)
                return


    def convert(self, url: str, name_salt: str) -> subprocess.Popen:
        """
        Compile the command, and all the flags provided, and then
        run it on the commmand line as a subprocess.
        """

        # For us to positively identify the downloaded file for follow_up() later,
        # we add a salt to the final output name.
        self.flags_and_args[2] = f'-o{name_salt}-%(title)s.%(etx)s'

        self.command.append(self.app)
        self.command[1:1] = self.flags_and_args
        self.command.append(url)

        # Return the process, so we can check stdout/stderr
        proc = subprocess.Popen(self.command, stdout=PIPE, stderr=PIPE)

        return proc
