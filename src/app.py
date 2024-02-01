"""
  Main module for KAVACH2.0-A password manager.
  This is the entry point of the project.
"""
import logging
from config.prompts.logprompts import LogPrompts
from config.prompts.prompts import Prompts
from dependency_container.container import DependencyContainer
from config.app_config import AppConfig
from database_layer.database import db
from dependency_container.inject_auth_dependency import inject_auth_dependency

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s %(funcName)s:%(lineno)d] %(message)s',
    level=logging.DEBUG,
    filename=AppConfig.LOG_FILE_PATH
)
logger = logging.getLogger(__name__)
Prompts.load()
db.create_all_tables()

if __name__ == "__main__":
    logger.info(LogPrompts.KAVACH_MAIN_MODULE_STARTING)
    print(Prompts.KAVACH_STARTING)
    inject_auth_dependency()
    auth = DependencyContainer.auth_dashboard
    auth.login_user()
    logger.info(LogPrompts.KAVACH_MAIN_MODULE_ENDED)


