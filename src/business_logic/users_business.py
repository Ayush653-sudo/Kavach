"""
This module deals with business logics and database of our program.
"""
from config.prompts.prompts import Prompts
from config.query import QueryConfig
from database_layer.database import db
from helpers.exceptions.not_found import NotFoundError


class UserBusiness:
    """

    """
    def get_all_users(self) -> list:

        get_all_users = db.fetch_data_from_database(QueryConfig.GET_USERS)
        return get_all_users

    def inactive_user(self, user_name: str) -> None:
        get_all_users = db.fetch_data_from_database(QueryConfig.GET_ALL_USERS)

        for user in get_all_users:
            if user[0] == user_name:
                db.add_data_to_database(QueryConfig.update_USERS, ("inactive", user_name))
                return

        raise NotFoundError(Prompts.SORRY_NO_DATA)



