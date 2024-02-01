"""Module for loading prompts of project."""
import yaml

from config.app_config import AppConfig


class Prompts:
    """
        This class contains methods for loading prompts from yaml file.
        ...
        Methods
        -------
        load() -> None:
            This method loads the variables from yaml to py.
    """
    KAVACH_STARTING = None
    REGULAR_USER_MENU = None
    ENTER_CHOICE = None
    PASSWORD_TO_CHECK_STRENGTH = None
    LENGTH_FOR_PASSWORD = None
    HI_USER = None
    PASSWORD_DASHBOARD_MENU = None
    ENTER_WEBSITE_URL = None
    ENTER_PASSWORD = None
    ENTER_PASSWORD_TYPE = None
    SOMETHING_WENT_WRONG = None
    ENTER_PASSWORD_ID_TO_SEE = None
    ENTER_PASSWORD_ID_TO_UPDATE = None
    ENTER_UPDATED_PASSWORD = None
    ENTER_PASSWORD_ID_TO_DELETED = None
    ENTER_USERNAME = None
    ENTER_EMAIL = None
    ENTER_PHONE_NUMBER = None
    LOGIN_ATTEMPT_LEFT = None
    ENTER_LOGIN_DETAILS = None
    LOGIN_OR_REGISTER_CHOICE = None
    MAXIMUM_ATTEMPT_REACHED = None
    EXIT_OR_NOT = None
    PASSWORD_UPDATED_SUCESSFULLY = None
    PASSWORD_DELETED_SUCCESSFULLY = None
    PASSWORD_ADDED_SUCCESSFULLY = None
    USER_DELETED_SUCCESSFULLY = None
    USER_REGISTERED_SUCCESSFULLY = None
    SORRY_NO_DATA = None
    DUBLICATE_KEY = None
    AUDIT_MENU = None
    ENTER_PASSWORD_ID_TO_FETCH_AUDIT = None
    INTEGRITY_ERROR_MESSAGE = None
    OPERATIONAL_ERROR_MESSAGE = None
    PROGRAMMING_ERROR_MESSAGE = None
    GENERAL_EXCEPTION_MESSAGE = None
    YOU_CANT_DELETE_YOURSELF = None

    @classmethod
    def load(cls) -> None:
        """
                    Method to load variables from yaml to py
                    Parameters = cls
                    Return Type = None
        """
        with open(AppConfig.PROMPT_PATH, "r") as file:
            data = yaml.safe_load(file)
            cls.KAVACH_STARTING = data["KAVACH_STARTING"]
            cls.REGULAR_USER_MENU = data["REGULAR_USER_MENU"]
            cls.ENTER_CHOICE = data["ENTER_CHOICE"]
            cls.PASSWORD_TO_CHECK_STRENGTH = data["PASSWORD_TO_CHECK_STRENGTH"]
            cls.LENGTH_FOR_PASSWORD = data["LENGTH_FOR_PASSWORD"]
            cls.HI_USER = data["HI_USER"]
            cls.ENTER_USERNAME = data["ENTER_USERNAME"]
            cls.PASSWORD_DASHBOARD_MENU = data["PASSWORD_DASHBOARD_MENU"]
            cls.ENTER_WEBSITE_URL = data["ENTER_WEBSITE_URL"]
            cls.ENTER_PASSWORD = data["ENTER_PASSWORD"]
            cls.ENTER_PASSWORD_TYPE = data["ENTER_PASSWORD_TYPE"]
            cls.SOMETHING_WENT_WRONG = data["SOMETHING_WENT_WRONG"]
            cls.ENTER_PASSWORD_ID_TO_SEE = data["ENTER_PASSWORD_ID_TO_SEE"]
            cls.ENTER_PASSWORD_ID_TO_UPDATE = data["ENTER_PASSWORD_ID_TO_UPDATE"]
            cls.ENTER_UPDATED_PASSWORD = data["ENTER_UPDATED_PASSWORD"]
            cls.ENTER_PASSWORD_ID_TO_DELETED = data["ENTER_PASSWORD_ID_TO_DELETED"]
            cls.ENTER_PASSWORD = data["ENTER_PASSWORD"]
            cls.ENTER_EMAIL = data["ENTER_EMAIL"]
            cls.ENTER_PHONE_NUMBER = data["ENTER_PHONE_NUMBER"]
            cls.LOGIN_ATTEMPT_LEFT = data["LOGIN_ATTEMPT_LEFT"]
            cls.ENTER_LOGIN_DETAILS = data["ENTER_LOGIN_DETAILS"]
            cls.LOGIN_OR_REGISTER_CHOICE = data["LOGIN_OR_REGISTER_CHOICE"]
            cls.MAXIMUM_ATTEMPT_REACHED = data["MAXIMUM_ATTEMPT_REACHED"]
            cls.EXIT_OR_NOT = data["EXIT_OR_NOT"]
            cls.PASSWORD_UPDATED_SUCESSFULLY = data["PASSWORD_UPDATED_SUCESSFULLY"]
            cls.PASSWORD_DELETED_SUCCESSFULLY = data["PASSWORD_DELETED_SUCCESSFULLY"]
            cls.PASSWORD_ADDED_SUCCESSFULLY = data["PASSWORD_ADDED_SUCCESSFULLY"]
            cls.USER_DELETED_SUCCESSFULLY = data["USER_DELETED_SUCCESSFULLY"]
            cls.USER_REGISTERED_SUCCESSFULLY = data["USER_REGISTERED_SUCCESSFULLY"]
            cls.SORRY_NO_DATA = data["SORRY_NO_DATA"]
            cls.DUBLICATE_KEY = data["DUBLICATE_KEY"]
            cls.AUDIT_MENU = data["AUDIT_MENU"]
            cls.ENTER_PASSWORD_ID_TO_FETCH_AUDIT = data["ENTER_PASSWORD_ID_TO_FETCH_AUDIT"]
            cls.INTEGRITY_ERROR_MESSAGE = data["INTEGRITY_ERROR_MESSAGE"]
            cls.OPERATIONAL_ERROR_MESSAGE = data["INTEGRITY_ERROR_MESSAGE"]
            cls.PROGRAMMING_ERROR_MESSAGE = data["PROGRAMMING_ERROR_MESSAGE"]
            cls.GENERAL_EXCEPTION_MESSAGE = data["GENERAL_EXCEPTION_MESSAGE"]
            cls.YOU_CANT_DELETE_YOURSELF = data["YOU_CANT_DELETE_YOURSELF"]


