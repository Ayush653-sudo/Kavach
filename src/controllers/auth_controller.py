"""
    Module for dealing with auth_view and calling auth_business
    The user password is stored in hashed format.

"""


import logging
from config.prompts.prompts import Prompts
from business_logic.auth_business import AuthBusiness
from helpers.decorators import error_handler
from models.users import User


logger = logging.getLogger('auth_controller')


class AuthController:
    """
    This class is of managing authentication related deals

    Methods:
    ----------
    register_user() ->method for registration purpose.
    login()->method to log in the user.
    logout()-> method to make user's logout.

    """
    def __init__(self, auth_business):
        self.auth_business = auth_business

    @error_handler
    def register_user(self, user_data: User) -> str:
        """
       This method will handle registration related user request and response
        :param user_data:
        :return->None:
        """
        self.auth_business.register_user_to_db(user_data)
        return Prompts.USER_REGISTERED_SUCCESSFULLY

    @error_handler
    def login_user(self, login_data: tuple) -> User:
        """
        This method will do user's login related request and response
        :param login_data:
        :return ->User:
        """
        user = self.auth_business.get_user_by_username_and_password(login_data)
        return user






