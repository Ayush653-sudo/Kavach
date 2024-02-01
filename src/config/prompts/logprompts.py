

import yaml
from config.app_config import AppConfig


class LogPrompts:
    KAVACH_MAIN_MODULE_STARTING = None
    KAVACH_MAIN_MODULE_ENDED = None
    KAVACH_PAUSED = None
    SYSTEM_RESUMED = None
    REDUCING_LOGIN_ATTEMPTS = None
    ENTERIGNG_LOOP = None
    VALIDATING_INPUT = None
    INVALID_INPUT = None
    CREATED_AUDITS_TABLE = None
    CREATED_PASSWORDS_TABLE = None
    CREATED_REGISTRATIONS_TABLE = None
    CREATED_KEYS_TABLE = None
    DATA_SAVED_DATABASE = None
    DATA_FETCHED_FROM_DATABASE = None
    EXITING_LOOP = None

    @classmethod
    def load(cls) -> None:
        """
                    Method to load variables from yaml to py
                    Parameters = cls
                    Return Type = None
        """
        with open(AppConfig.LOGPROMPT_PATH, "r") as file:
            data = yaml.safe_load(file)
            cls.KAVACH_MAIN_MODULE_STARTING = data["KAVACH_MAIN_MODULE_STARTING"]
            cls.KAVACH_MAIN_MODULE_ENDED = data["KAVACH_MAIN_MODULE_ENDED"]
            cls.KAVACH_PAUSED = data["KAVACH_PAUSED"]
            cls.SYSTEM_RESUMED = data["SYSTEM_RESUMED"]
            cls.REDUCING_LOGIN_ATTEMPTS = data["REDUCING_LOGIN_ATTEMPTS"]
            cls.ENTERIGNG_LOOP = data["ENTERIGNG_LOOP"]
            cls.VALIDATING_INPUT = data["VALIDATING_INPUT"]
            cls.INVALID_INPUT = data["INVALID_INPUT"]
            cls.CREATED_PASSWORDS_TABLE = data["CREATED_PASSWORDS_TABLE"]
            cls.CREATED_AUDITS_TABLE = data["CREATED_AUDITS_TABLE"]
            cls.CREATED_REGISTRATIONS_TABLE = data["CREATED_REGISTRATIONS_TABLE"]
            cls.CREATED_KEYS_TABLE = data["CREATED_KEYS_TABLE"]
            cls.DATA_SAVED_DATABASE = data["DATA_SAVED_DATABASE"]
            cls.DATA_FETCHED_FROM_DATABASE = data["DATA_FETCHED_FROM_DATABASE"]
            cls.EXITING_LOOP = data["EXITING_LOOP"]