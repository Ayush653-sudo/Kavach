"""
This module deals ui part of  password audits related tasks
"""

from config.app_config import AppConfig
from config.prompts.prompts import Prompts
from enums.password_starter import PasswordStarter
from helpers.decorators import looper
from enums.audit_operation import AuditOperation
from models.users import User
from helpers.common import display_table
from views.table_headers.password_audit_header import PASSWORD_DETAIL_HEADER


class PasswordAuditDashboard:
    """
    This is class representig paasword audits related with user.
    """
    def __init__(self,user: User ,audit_controller) -> None:
        self.user = user
        self.audit_controller = audit_controller
        
    
    @looper
    def menu(self):
        print(Prompts.AUDIT_MENU)
        choice = input(Prompts.ENTER_CHOICE)
        match choice:
            case AuditOperation.FETCHED.value:
                self.view_password_fetched_audits()
            case AuditOperation.UPDATED.value:
                self.view_password_update_audits()
            case AuditOperation.ADDED.value:
                self.view_password_Initial_audits()
            case AuditOperation.GOBACK.value:
                return True            
             
        return False
    
    def view_password_fetched_audits(self):
        
        password_id = input(Prompts.ENTER_PASSWORD_ID_TO_FETCH_AUDIT).strip()
        result = self.audit_controller.get_password_fetched_audit(password_id, AppConfig.FETCHED,self.user.username)
        display_table(result, PASSWORD_DETAIL_HEADER)

    def view_password_update_audits(self):
        password_id = input(Prompts.ENTER_PASSWORD_ID_TO_FETCH_AUDIT).strip()
        result = self.audit_controller.get_password_fetched_audit(password_id, AppConfig.UPDATED,self.user.username)
        display_table(result, PASSWORD_DETAIL_HEADER)

    def view_password_Initial_audits(self):
        password_id = input(Prompts.ENTER_PASSWORD_ID_TO_FETCH_AUDIT).strip()
        result = self.audit_controller.get_password_fetched_audit(password_id, AppConfig.INITIAL,self.user.username)
        display_table(result, PASSWORD_DETAIL_HEADER)

        

    


