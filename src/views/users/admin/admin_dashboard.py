"""
This module represent admin dashboard
"""
from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from dependency_container.container import DependencyContainer
from enums.admin_starter import AdminStarter
from helpers.common import display_table
from helpers.decorators import looper
from models.users import User
from views.table_headers.user_details_header import USER_DETAILS_HEADER
import sys

class AdminDashboard:

    def __init__(self, user: User, user_controller) -> None:
        self.user = user
        self.user_controller = user_controller


    def menu(self) -> None:
        """
        This function will show menu bar of admin dashboard
        :return:None
        """
        while True:
            print(Prompts.HI_USER.format(self.user.username))
            print(Prompts.ADMIN_DASHBOARD)
            choice = input(Prompts.ENTER_CHOICE)
            match choice:
                case AdminStarter.Add_NEW_ADMIN.value:
                    self.add_new_admin()
                case AdminStarter.SEE_USERS.value:
                    self.see_users_view()
                case AdminStarter.DELETE_USER.value:
                    self.delete_users_view()
                case AdminStarter.Exit.value:
                    self.user = None
                    sys.exit()

    def add_new_admin(self):
        """
        This function will add_new_admin
        :return:
        """
        auth_dashboard = DependencyContainer.auth_dashboard
        auth_dashboard.user_registration(AppConfig.Admin)

    def see_users_view(self) -> None:
        """
        display user's details
        :return:
        """
        result = self.user_controller.get_all_user(self.user)
        display_table(result, USER_DETAILS_HEADER)

    def delete_users_view(self) -> None:
        """
        display all users and delete any by entering their username.

        :return: None
        """
        result = self.user_controller.get_all_user(self.user)
        display_table(result, USER_DETAILS_HEADER)
        choosen_username = input(Prompts.ENTER_USERNAME).strip()
        result = self.user_controller.delete_user_by_username(choosen_username,self.user)
        if result:
            print(result)
        else :
            print(Prompts.SOMETHING_WENT_WRONG)




