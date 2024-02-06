"""
This module contains all necessary operation perform by any regular user of our platform.
"""
import sys

from config.prompts.prompts import Prompts
from enums.regular_user_starter import RegularUserStarter
from helpers.decorators import error_handler, looper
from views.users.regular.password_dashboard import PasswordDashboard


class RegularUserDashboard:
    """
    This class shows the dashboard of Regular user
    attributes:->user , password_controller
    methods:-
    menu()
    check_password_strength()
    generate_password()
    """
    def __init__(self, user, password_controller):
        self.user = user
        self.password_controller = password_controller

    
    def menu(self) -> None:
        """
        This method shows only the menu
        :return: bool
        """
        while True:
            print(Prompts.HI_USER.format(self.user.username))
            print(Prompts.REGULAR_USER_MENU)
            choice = input(Prompts.ENTER_CHOICE)
            match choice:
                case RegularUserStarter.CheckStrength.value:
                    self.check_password_strength()
                case RegularUserStarter.GeneratePassword.value:
                    self.generate_password()
                case RegularUserStarter.OpenPasswordDashboard.value:
                    password_dashboard = PasswordDashboard(self.user, self.password_controller)
                    password_dashboard.menu()
                case RegularUserStarter.Exit.value:
                     sys.exit()
       
        

    def check_password_strength(self) -> None:
        """
        This method will show how weak or strong your password or how many times it is breaken is
        :return None:
        """
        password = input(Prompts.PASSWORD_TO_CHECK_STRENGTH)
        messages = self.password_controller.check_password(password)
        for message in messages:
            print(message)
            print()
        

    @error_handler
    def generate_password(self) -> None:
        """
        This method will generate any random password.
        :return None:
        """
        length = int(input(Prompts.LENGTH_FOR_PASSWORD))
        generated_password = self.password_controller.generate_password(length)
        if  generated_password:
            print(generated_password+"\n")
            

