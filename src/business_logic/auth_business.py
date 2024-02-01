"""
    Module for authenticating purpose of users(both admin and Regular) based on their credentials.
    The user password is stored in hashed format.

"""


import logging
import hashlib
from config.prompts.prompts import Prompts
from database_layer.database import db
from config.query import QueryConfig
from helpers.exceptions.dublicate_error import DuplicateError
from cryptography.fernet import Fernet
from helpers.exceptions.not_found import NotFoundError
from models.users import User
logger = logging.getLogger('auth_business')


class AuthBusiness:
    """
    This class deals with database layer and authentication related operation.

    """
    def register_user_to_db(self, user_data: User) -> None:
        """

        :param self, user_data:
        :return -> None:
        """
        user_data.password = hashlib.sha256(user_data.password.encode('utf-8')).hexdigest()
        get_all_users = db.fetch_data_from_database(QueryConfig.GET_ALL_USERS)
        user_with_same_username = [user for user in get_all_users if user[0] == user_data.username]
        if len(user_with_same_username) > 0:
            raise DuplicateError(Prompts.DUBLICATE_KEY)
        db.add_data_to_database(
            QueryConfig.CREATE_USER_CREDENTIALS,
            (user_data.username, user_data.password, user_data.phone_number,
             user_data.email_address, user_data.role, user_data.status)
        )
        key = Fernet.generate_key()+user_data.username.encode()
        db.add_data_to_database(QueryConfig.INSERT_KEY_INTO_TABLE, (user_data.username, key))

    def get_user_by_username_and_password(self, login_data) -> type(User):
        get_all_users = db.fetch_data_from_database(QueryConfig.GET_ALL_USERS)
        user_name = login_data[0]
        hashed_password = hashlib.sha256(login_data[1].encode('utf-8')).hexdigest()
        user_with_given_username_and_password = [user for user in get_all_users
                                                 if user[0] == user_name and
                                                 user[1] == hashed_password and user[5] == "active"]
        if user_with_given_username_and_password:
            user = User(user_with_given_username_and_password[0][0], user_with_given_username_and_password[0][1],
                        user_with_given_username_and_password[0][2], user_with_given_username_and_password[0][3],
                        user_with_given_username_and_password[0][4])
            return user
        raise NotFoundError(Prompts.SORRY_NO_DATA)










