from threading import Lock
from typing import List
from dotenv import dotenv_values

import sys

class SingletonMeta(type):
    """
    Thread-safe implementation of Singleton.
    """

    _instances = {}
    _lock: Lock = Lock()
    """
    The lock object will be used to synchronize threads during
    first access to the Singleton.
    """
    def __call__(cls, *args, **kwargs):
        """
        Now imagine that the program has just been launched. Since
        there's no Singleton instance yet, multiple threads can simultaenouly
        pass the previous conditional and reach this point almost at the same time.

        The first of them will acquire lock and will proceed further, while the rest
        will wait here.
        """
        with cls._lock:
            # The first thread to acquire the lock reaches this conditional,
            # goes inside and creates the Singleton instance. Once it leaves the
            # lock block, a thread that might have been waiting for the lock
            # release may then enter this section. But since the Singleton field
            # is already initialized, the thread won't create a new object.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class Configs(metaclass=SingletonMeta):
    """
    Configs that source private environment variables.
    """
    config = dotenv_values(".env")

    try:
        __email_address: str = config["EMAIL_ADDRESS"] or ""
        __email_password: str = config["EMAIL_PASS"] or ""

    except KeyError as error:
        sys.stderr.write(f"Dotenv config error: {error} is missing\n")
        sys.exit(1)

    @classmethod
    @property
    def email_address(cls) -> str:
        """
        Getter for the e-mail address
        """
        return cls.__email_address

    @classmethod
    @property
    def email_password(cls) -> str:
        """
        Getter for the e-mail password
        """
        return cls.__email_password

class ConversionQueue(metaclass=SingletonMeta):
    queue: List[List] = []
    """
    Keep a record of the conversion requests.
    """

    @classmethod
    def push(cls, request: dict, output_name_salt: str) -> None:
        """
        Add onto queue. This will be checked by
        """
        cls.queue.append([request, output_name_salt])
