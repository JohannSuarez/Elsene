from typing import List
import subprocess
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
            '-o ~/%(title)s.%(etx)s',
            '--audio-format',
            'mp3'
        ]

    @staticmethod
    def follow_up() -> None:
        """
        Manages the downloaded file, calling Mailer on it, and cleaning up afterwards.
        """

    def convert(self, url: str) -> subprocess.Popen:
        """
        Compile the command, and all the flags provided, and then
        run it on the commmand line as a subprocess.
        """
        self.command.append(self.app)
        self.command[1:1] = self.flags_and_args
        self.command.append(url)

        # Return the process, so we can check stdout/stderr
        proc = subprocess.Popen(self.command, stdout=PIPE, stderr=PIPE)
        return proc
