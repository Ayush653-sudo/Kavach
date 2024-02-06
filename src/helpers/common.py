"""
This module contain common functionalities like input validation etc
"""

import logging
import re
from tabulate import tabulate

from config.prompts.logprompts import LogPrompts
logger = logging.getLogger(__name__)


def is_input_validation(regular_exp: str, input_field: str) -> bool:
    """
        Method to validate input on basis of regex.
        Parameter -> regular_exp: str, input_field: str
        Return type -> bool
    """
    logger.info(LogPrompts.VALIDATING_INPUT)
    result = re.search(regular_exp, input_field)
    if result:
        return True
    else:
        logger.debug(LogPrompts.INVALID_INPUT)
        return False


def display_table(data: list, headers: list) -> None:
    """
     Method to display data in tabular format using tabulate.
     Parameter -> data: list, headers: list
    Return type -> None

    """

    row_id = [i for i in range(1, len(data) + 1)]
    print(
        tabulate(
            data,
            headers,
            showindex=row_id,
            tablefmt="simple_grid"
            )
        )
