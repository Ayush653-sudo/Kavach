"""
This module deal with client user's related request and also give necessary response.
"""
from config.prompts.prompts import Prompts
from config.app_config import AppConfig
from business_logic.users_business import UserBusiness
from helpers.decorators import error_handler
from models.users import User


class UsersController:
    """
    This class deal with rendering user's related operations.

    """
    def __init__(self, user_business):
        self.user_business = user_business

    def get_all_user(self, user: User) -> list:
        if user.role == AppConfig.Admin:
            return self.user_business.get_all_users()


    @error_handler
    def delete_user_by_username(self, to_delete_user_name: str, user:User) -> str:
        if user.username != to_delete_user_name:
            self.user_business.inactive_user(to_delete_user_name)
            return Prompts.USER_DELETED_SUCCESSFULLY.format(to_delete_user_name)
        else:
            return Prompts.YOU_CANT_DELETE_YOURSELF
