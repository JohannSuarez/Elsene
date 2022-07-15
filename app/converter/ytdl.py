from typing import List
import subprocess
from subprocess import PIPE


#subprocess.run(["youtube-dl", "--extract-audio", "--audio-format", "mp3", "-o", "filename.mp3", "https://www.youtube.com/watch?v=r26VsCGCgb0"])
#subprocess.run(["youtube-dl", "--extract-audio", "--restrict-filenames", "--audio-format", "mp3", "https://www.youtube.com/watch?v=r26VsCGCgb0"])

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
            '--audio-format',
            'mp3'
        ]

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


