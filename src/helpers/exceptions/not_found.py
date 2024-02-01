"""
This module is only for generating custom exceptions
"""


class NotFoundError(Exception):
    """
    This class is for generating custom exception in case of data not found.
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


