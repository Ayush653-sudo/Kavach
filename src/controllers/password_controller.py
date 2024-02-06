"""
This module is only for rendering Regular user request
"""
from config.prompts.prompts import Prompts
from config.app_config import AppConfig
from business_logic.password_business import PasswordBusiness
from helpers.decorators import error_handler
from models.password import Password
from business_logic.audit_business import AuditBusiness
from models.audit_password import AuditPassword


class PasswordController:
    """
    This class intermediate between user's request and business logic and also
    responsible to give response to user
    methods:->
    check_password()
    generate_password()
    add_new_password()
    get_decrypted_password_by_id()
    update_password()
    delete_password_by_id()
    """
    def __init__(self,password_business,audit_business):
        self.password_business = password_business
        self.audit_business = audit_business

    def check_password(self, password: str) -> list:
        """
        This method take password input from user and give response about it's strength
        :param password:
        :return:
        """
        return self.password_business.check_password_strength(password)

    @error_handler
    def generate_password(self, length: int) -> str:
        """
        This method take length and pass it over business logic
        it will give response as strong generated password
        :param length:
        :return:
        """
        return self.password_business.generate_password(length)

    @error_handler
    def add_new_password(self, password: Password) -> str:
        """
        This method will add new password
        :param password:
        :return:
        """
        self.password_business.add_password(password)
        audit_password = AuditPassword(password.id, AppConfig.INITIAL, password.user_name)
        self.audit_business.add_audit_password(audit_password)
        return Prompts.PASSWORD_ADDED_SUCCESSFULLY

    def get_passwords_by_username(self, user_name: str) -> list:
        """
        This method will deal with getting password related task of user's
        :param user_name:
        :return:
        """
        get_all_passwords = self.password_business.get_password_by_username(user_name)
        return get_all_passwords

    @error_handler
    def get_decrypted_password_by_id(self, id1: str, user_name: str) -> list:
        get_decrypted_password = self.password_business.get_decrypted_password(id1, user_name)
        if get_decrypted_password:
            audit_password = AuditPassword(id1, AppConfig.FETCHED,user_name)
            self.audit_business.add_audit_password(audit_password)
            return get_decrypted_password

    @error_handler
    def update_password(self, id1: str, user_name: str, updated_password: str) -> str:
        self.password_business.update_password(id1, user_name, updated_password)
        audit_password = AuditPassword(id1, AppConfig.UPDATED, user_name)
        self.audit_business.add_audit_password(audit_password)
        return Prompts.PASSWORD_UPDATED_SUCESSFULLY 

    @error_handler
    def delete_password_by_id(self, id1: str, user_name: str) -> str:
        self.password_business.delete_password(id1, user_name)
        return Prompts.PASSWORD_DELETED_SUCCESSFULLY





