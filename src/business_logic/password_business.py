"""
This is for implementing regular user request and managing it's related database operation.
"""
from config.prompts.prompts import Prompts
from config.app_config import AppConfig
from config.query import QueryConfig
from database_layer.database import db
from helpers.exceptions.not_found import NotFoundError
from helpers.exceptions.range_error import RangeError
from helpers.password_strength import check_strength
import random
from datetime import datetime
from cryptography.fernet import Fernet

from models.password import Password


class PasswordBusiness:
    """
    This class handle regular user business

    method: check_password_strength() ->check strength of password
            generate_password() -> generate strong random password

    """
    def check_password_strength(self, password: str) -> list:
        """
        :param password:
        :return ->list:
        """
        return check_strength(password)

    def generate_password(self, length: int) -> str:
        """
        This function would generate strong password
        :param length:
        :return:
        """
        if length < 8:
            raise RangeError("You must enter length grater than or equal to 8")
        combined_list = (AppConfig.DIGITS + AppConfig.UPPERCASE_CHARACTERS +
                         AppConfig.LOWERCASE_CHARACTERS + AppConfig.SYMBOLS)
        rand_digit = random.choice(AppConfig.DIGITS)
        rand_upper = random.choice(AppConfig.UPPERCASE_CHARACTERS)
        rand_lower = random.choice(AppConfig.LOWERCASE_CHARACTERS)
        rand_symbol = random.choice(AppConfig.SYMBOLS)
        temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
        for x in range(length - 4):
            temp_pass = temp_pass + random.choice(combined_list)
        return temp_pass

    def add_password(self, password: Password) -> None:

        keys = db.fetch_data_from_database(QueryConfig.GET_ALL_KEY, (password.user_name,))
        user_secret_key = keys[0][1]
        fernet = Fernet(user_secret_key+AppConfig.SECRET_KEY.encode())
        password.password = fernet.encrypt(password.password.encode())
        db.add_data_to_database(QueryConfig.INSERT_PASSWORD_INTO_TABLE, (password.id, password.user_name,
                                                                         password.website_url, password.password,
                                                                         password.password_type, password.last_updated))

    def get_password_by_username(self, user_name: str) -> list:
        list_of_passwords = db.fetch_data_from_database(QueryConfig.GET_ALL_PASSWORD, (user_name,))
        return list_of_passwords

    def get_decrypted_password(self, id1: str, user_name: str) -> list:
        list_of_passwords_and_keys = db.fetch_data_from_database(QueryConfig.GET_ENCRYP_PASSWORD_AND_KEY,(id1,user_name))
        for password , key in list_of_passwords_and_keys:
            fernet = Fernet(key + AppConfig.SECRET_KEY.encode())
            result = fernet.decrypt(password).decode()
            final = (id1,result)
            return [final]
        raise NotFoundError(Prompts.SORRY_NO_DATA)

    def update_password(self, id1: str, user_name: str, updated_password: str):
        keys = db.fetch_data_from_database(QueryConfig.GET_ALL_KEY, (user_name,))
        fernet = Fernet(keys[0][1] + AppConfig.SECRET_KEY.encode())
        updated_password = fernet.encrypt(updated_password.encode())
        list_of_passwords = self.get_password_by_username(user_name)
        for obj in list_of_passwords:
            if obj[0] == id1:
                db.add_data_to_database(QueryConfig.UPDATE_PASSWORD, (updated_password, datetime.now(), user_name, id1))
                return

        raise NotFoundError(Prompts.SORRY_NO_DATA)

    def delete_password(self, id1: str, user_name: str) -> None:
        list_of_passwords = self.get_password_by_username(user_name)
        for password_id, username, url,operation in list_of_passwords:
            if password_id == id1:
                db.add_data_to_database(QueryConfig.DELETE_PASSWORD_FROM_TABLE, (id1,))
                return

        raise NotFoundError(Prompts.SORRY_NO_DATA)




