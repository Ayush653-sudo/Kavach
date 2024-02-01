"""
This module is only to check strength of any password
"""
from config.app_config import AppConfig
from config.regex_pattern import RegexPattern
from helpers.common import is_input_validation


def check_strength(password):
    """
    This method will check strength of  password
    """
    strength_message=[]
    time_used = most_common_password(password)
    if time_used:
        strength_message.append(f"your entered password is already in use  {time_used} times"+
                                f" and among most common password list")

    if not is_input_validation(RegexPattern.HAS_NUMBER, password):
        strength_message.append("Your Password should contain at least one number ")
    if not is_input_validation(RegexPattern.HAS_SYMBOL, password):
        strength_message.append("Your Password should contain at least one special symbol ")
    if not is_input_validation(RegexPattern.HAS_LOWER_CHARACTER, password):
        strength_message.append("Your Password should contain at least one special symbol ")
    if not is_input_validation(RegexPattern.HAS_UPPER_CHARACTER, password):
        strength_message.append("your password should contain at least upper character ")
    if len(strength_message) == 0:
        strength_message.append("Your password is strong enough")
    return strength_message


def most_common_password(password):
    with open(AppConfig.COMMON_PASSWORD_FILE,"r") as file:
        content = file.readlines()
        for leak_pass in content:
            leak_pass_obj = leak_pass.split("-")
            if leak_pass_obj[0] == password:
                return leak_pass_obj[1]

    file.close()



