"""Module containing decorators used throughout the project."""
from functools import wraps
import logging
import sqlite3
from typing import Callable
from config.prompts.prompts import Prompts
from config.prompts.logprompts import LogPrompts

from helpers.exceptions.dublicate_error import DuplicateError
from helpers.exceptions.not_found import NotFoundError
from helpers.exceptions.range_error import RangeError
from helpers.error.error_response import ErrorResponse
Prompts.load()
logger = logging.getLogger(__name__)


def error_handler(func: Callable) -> Callable:
    """
        Decorator function for handling sqlite3 exceptions happening in project.
        Parameter -> function: Callable
        Return type -> wrapper: Callable
    """
    @wraps(func)
    def wrapper(*args: tuple, **kwargs: dict) -> ErrorResponse:
        """
            Wrapper function for executing the function and handling exception whenever occur.
            Parameter -> *args: tuple, **kwargs: dict
            Return type -> ErrorResponse
        """
        try:
            return func(*args, **kwargs)
        except RangeError as error:
            logger.exception(error.message)
            return ErrorResponse(error.message)
        except NotFoundError as error:
            logger.exception(error.message)
            return ErrorResponse(error.message)
        except DuplicateError as error:
            logger.exception(error.message)
            return ErrorResponse(error.message)
        except sqlite3.IntegrityError as error:
            logger.exception(error)
            return ErrorResponse(Prompts.INTEGRITY_ERROR_MESSAGE)
        except sqlite3.OperationalError as error:
            logger.exception(error)
            return ErrorResponse(Prompts.OPERATIONAL_ERROR_MESSAGE )
        except sqlite3.ProgrammingError as error:
            logger.exception(error)
            return ErrorResponse(Prompts.PROGRAMMING_ERROR_MESSAGE)
        except sqlite3.Error as error:
            logger.exception(error)
            return ErrorResponse(Prompts.GENERAL_EXCEPTION_MESSAGE )
        except Exception as error:
            logger.exception(error)
            return ErrorResponse(Prompts.GENERAL_EXCEPTION_MESSAGE )

    return wrapper


def looper(func: Callable) -> Callable:
    """
        Decorator function for making the func loop until a condition is satisfied.
        Parameter -> func: Callable
        Return type -> wrapper: Callable
    """
    @wraps(func)
    def wrapper(*args: tuple, **kwargs: tuple) -> bool | str | int:
        """
            Wrapper function to loop the function until function returns True.
            Parameter -> *args: tuple, **kwargs: dict
            Return type -> bool | str | int
        """
        logger.info(LogPrompts.ENTERIGNG_LOOP)
        while True:
            result = func(*args, **kwargs)
            if result:
                logger.info(LogPrompts.EXITING_LOOP)
                return result
    return wrapper

