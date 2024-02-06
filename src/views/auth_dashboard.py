"""
This module show Authentication dashboard for the user's
"""

import logging
import time

import maskpass
from dependency_container.inject_audit_dependency import injecting_audit_dependency
from views.input_taker import InputTaker
from config.prompts.logprompts import LogPrompts
from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from dependency_container.container import DependencyContainer
from dependency_container.inject_admin_dependency import inject_admin_user_dependency
from dependency_container.inject_regular_user_dependency import inject_regular_user_dependency
from helpers.decorators import looper
from models.users import User



logger = logging.getLogger(__name__)


class AuthDashboard:
    """
          Class containing method for taking user login credentials  as input and user registration .
          ...
          Attribute
          ---------
          max_login_attempts (private) -> Maximum login attempts with user for valid login (i.e. 3)

          Methods
          -------
          login() -> Method for taking login credentials as input.
          logout() -> Method through which user can log out to their account.
      """

    def __init__(self, auth_controller) -> None:
        """
            Method for constructing auth views object.
            Parameters -> self
            Return type -> None
        """
        self.__max_login_attempts = AppConfig.MAXIMUM_LOGIN_ATTEMPTS
        self.auth_controller = auth_controller

    def user_registration(self, role):
        user_name = InputTaker.input_user_name()
        email = InputTaker.input_email()
        phone_number = InputTaker.input_phone_number()
        password = InputTaker.input_password()
        self.auth_controller.register_user(User(user_name, password, phone_number, email, role))

    @looper
    def login_user(self) -> bool:

        """
        method for managing user's login and rendering
         to registration if he/she do not have account.
        :return -> bool:
        """
        key_press = input(Prompts.LOGIN_OR_REGISTER_CHOICE).strip()
        if key_press == "1":
            self.user_registration(AppConfig.REGULAR)

        if self.__max_login_attempts == 0:
            logger.warning(LogPrompts.KAVACH_PAUSED)
            print(Prompts.MAXIMUM_ATTEMPT_REACHED)
            self.__max_login_attempts = AppConfig.MAXIMUM_LOGIN_ATTEMPTS
            time.sleep(10)
            logger.info(LogPrompts.SYSTEM_RESUMED)
        print(Prompts.ENTER_LOGIN_DETAILS)
        user_name = input(Prompts.ENTER_USERNAME).strip()
        password = maskpass.askpass(Prompts.ENTER_PASSWORD, mask="*").strip()
        user = self.auth_controller.login_user((user_name, password))

        if user:
            DependencyContainer.User = user
            if user.role == AppConfig.REGULAR:
                injecting_audit_dependency(user)
                inject_regular_user_dependency(user)
                regular_user_dashboard = DependencyContainer.regular_user_dashboard
                regular_user_dashboard.menu()
            elif user.role == AppConfig.Admin:
                inject_admin_user_dependency(user)
                admin_dashboard = DependencyContainer.admin_dashboard
                admin_dashboard.menu()
        else:
            logger.warning(LogPrompts.REDUCING_LOGIN_ATTEMPTS)
            self.__max_login_attempts -= 1
            print(Prompts.LOGIN_ATTEMPT_LEFT.format(self.__max_login_attempts))
            choice = input(Prompts.EXIT_OR_NOT)
            if choice in ("Y", "y"):
                return True












