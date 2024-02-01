"""
This module is only for generating custom exceptions
"""


class DuplicateError(Exception):
    """
    This class is for generating custom exception in case of inserting duplicate data.
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

