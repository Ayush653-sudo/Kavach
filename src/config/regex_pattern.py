"""
This module contain only regex pattern used throughout the Kavach
"""


class RegexPattern:
    """
    This class contains regex pattern only
    """
    HAS_NUMBER = r"[0-9]+"
    HAS_SYMBOL = r"[!@#$%^&*()_+=\[{\]};:<>|./?,-]"
    HAS_UPPER_CHARACTER = r"[A-Z]+"
    HAS_LOWER_CHARACTER = r"[a-z]+"
