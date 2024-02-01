import logging
import sqlite3
from typing import Optional
from config.prompts.logprompts import LogPrompts
from config.app_config import AppConfig
from config.query import QueryConfig


logger = logging.getLogger('db_logger')


class Database:
    """
    This class contains methods for executing database queries fetched from QueryConfig.
    ...
    Attributes
    ------------
    connection ->sqlite3.connection
    cursor -> sqlite3.Cursor

    Methods
    ---------
    create_all_tables()->Methods for creating all database tables.
    save_data_to_database() -> Method for saving data to a database.
    fetch_data_from_database() -> Method for fetching data from database tables.
    """
    def __init__(self):
        """
                  Method for initializing the sqlite3 connection and cursor object
                  Parameter -> self
                  Return type -> None
        """
        self.connection = sqlite3.connect(AppConfig.DATABASE_PATH)
        self.cursor = self.connection.cursor()
        logger.info("Successfully establish connection")

    def create_all_tables(self) -> None:
        """
                    Method for creating all tables of database
                    Parameter -> self
                    Return type -> None
        """
        self.cursor.execute(QueryConfig.User_Registration_TABLE_CREATION)
        logger.info(LogPrompts.CREATED_REGISTRATIONS_TABLE)
        self.cursor.execute(QueryConfig.KEY_TABLE_CREATION)
        logger.info(LogPrompts.CREATED_KEYS_TABLE)
        self.cursor.execute(QueryConfig.PASSWORD_TABLE_CREATION)
        logger.info(LogPrompts.CREATED_PASSWORDS_TABLE)
        self.cursor.execute(QueryConfig.CREATE_AUDIT_PASSWORD_TABLE)
        logger.info(LogPrompts.CREATED_AUDITS_TABLE)

    def add_data_to_database(self, query: str, data: tuple) -> None:
        """
                   Method for Adding data to single or multiple tables in database.
                   Parameter -> self, query: str, data: tuple
                   Return type -> None
        """
        self.cursor.execute(query, data)
        self.connection.commit()
        logger.info(LogPrompts.DATA_SAVED_DATABASE)

    def fetch_data_from_database(self, query: str, data: Optional[tuple] = None) -> list:
        """
                    Method for fetching data from database.
                    parameter -> self, query: str, data: Union[tuple, None]
                    Return type -> list
        """
        if data is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, data)
        logger.info(LogPrompts.DATA_FETCHED_FROM_DATABASE)
        return self.cursor.fetchall()


db = Database()