"""
This module is for password related operation.
"""
import sys

import maskpass
from views.table_headers.decrypted_password_head import PASSWORD_DECRYPTED_HEADER

from config.prompts.prompts import Prompts
from enums.password_starter import PasswordStarter
from helpers.common import display_table
from helpers.decorators import looper
from models.password import Password
from dependency_container.container import DependencyContainer
from dependency_container.inject_audit_dependency import injecting_audit_dependency
from views.table_headers.passwords_header import PASSWORD_DETAIL_HEADER


class PasswordDashboard:
    """
     This class deals with user's password related input
     and rendering it to controller layer and also show
     necessary output to user's
    """

    def __init__(self, user, password_controller):
        self.user = user
        self.password_controller = password_controller

    @looper
    def menu(self) -> bool:
        """
        This function is to show menubar and take user's choice as input
        :return -> bool:
        """
        print(Prompts.PASSWORD_DASHBOARD_MENU)
        choice = input(Prompts.ENTER_CHOICE)
        match choice:
            case PasswordStarter.AddPassword.value:
                self.add_new_password_view()
            case PasswordStarter.WatchPassword.value:
                self.see_passwords_view()
            case PasswordStarter.UpdatePassword.value:
                self.update_password_view()
            case PasswordStarter.DeletePassword.value:
                self.delete_password_view()
            case PasswordStarter.CheckPasswordAudits.value:
                injecting_audit_dependency(self.user)
                audit_dashboard = DependencyContainer.audit_dashboard
                audit_dashboard.menu()
            case PasswordStarter.GOBACK.value:
                return True
        return False

    def show_password_table(self):
        all_passwords = self.password_controller.get_passwords_by_username(self.user.username)
        if len(all_passwords) == 0:
            print(Prompts.SORRY_NO_DATA)
        display_table(all_passwords, PASSWORD_DETAIL_HEADER)

    def add_new_password_view(self) -> None:
        """
        This module is for taking user input to add new password
        :return:
        """
        website_url = input(Prompts.ENTER_WEBSITE_URL)
        password_input = maskpass.askpass(Prompts.ENTER_PASSWORD)
        password_type = input(Prompts.ENTER_PASSWORD_TYPE)
        password = Password(self.user.username, website_url, password_input, password_type)
        result = self.password_controller.add_new_password(password)
        if result:
            print(result)
        else:
            print(Prompts.SOMETHING_WENT_WRONG)

    def see_passwords_view(self) -> None:
        self.show_password_table()
        choice_id = input(Prompts.ENTER_PASSWORD_ID_TO_SEE).strip()
        if choice_id:
            decrypted_password = self.password_controller.get_decrypted_password_by_id(choice_id, self.user.username)
            if decrypted_password:
                display_table(decrypted_password, PASSWORD_DECRYPTED_HEADER)

    def update_password_view(self):
        self.show_password_table()
        chosen_id = input(Prompts.ENTER_PASSWORD_ID_TO_UPDATE)
        if chosen_id:
            new_password = input(Prompts.ENTER_UPDATED_PASSWORD)
            result = self.password_controller.update_password(chosen_id, self.user.username, new_password)
            if result:
                print(result)

    def delete_password_view(self):
        self.show_password_table()
        chosen_id = input(Prompts.ENTER_PASSWORD_ID_TO_DELETED)
        if chosen_id:
            result = self.password_controller.delete_password_by_id(chosen_id, self.user.username)
            print(result)
