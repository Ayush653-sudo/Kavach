
import maskpass
from config.prompts.prompts import Prompts
from helpers.decorators import looper
import re


class InputTaker:

    @staticmethod
    @looper
    def input_user_name() -> str:
        username = input(Prompts.ENTER_USERNAME).strip()
        hasOnlyAlphaNumeric = r"^[a-zA-Z][a-zA-Z0-9]*$"
        if re.fullmatch(hasOnlyAlphaNumeric,username):
            return username
        print("Enter username in alphanumeric order only\n")
    
    @staticmethod
    @looper
    def input_email() -> str:
        email = input(Prompts.ENTER_EMAIL).strip()
        emailRegex = r"^[^@\s]+@[^@\s]+\.(com|net|org|gov)$"
        if re.fullmatch(emailRegex,email):
            return email
        print("Please Enter email correctly\n")
        
    
    @staticmethod
    @looper
    def input_phone_number() ->str:
        hasnumber = r"^([0]|\+91)?[789]\d{9}$"
        phone_number = input(Prompts.ENTER_PHONE_NUMBER).strip()
        if re.fullmatch(hasnumber,phone_number):
            return phone_number
        print("please enter phone number correctly")
    
    @staticmethod
    @looper
    def input_password() ->str:
        hNumber = r"[0-9]+"
        has_upper_char = r"[A-Z]+"
        has_symbols = r"[!@#$%^&*()_+=\[{\]};:<>|./?,-]"
        has_lower_char = r"[a-z]"
        password = maskpass.askpass(Prompts.ENTER_PASSWORD, mask="*").strip()
        if re.search(hNumber,password) and re.search(has_upper_char,password) and re.search(has_symbols,password) and re.search(has_lower_char,password):
            return password
        print("Please enter strong password")
        
        


        
