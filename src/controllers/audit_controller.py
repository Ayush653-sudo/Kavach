"""
    Module for dealing with audit_view and calling audit_business

"""

from models.users import User


class AuditController:
    """
    This class do work of dealing with user's audit request and also give response to user 
    """
    def __init__(self, audit_business) -> None:
        self.audit_business = audit_business
        # print(self.audit_business)

    def get_password_fetched_audit(self,password_id: str, operation:str, user_name: str) ->list :
        result = self.audit_business.get_password_audit_by_status_from_db(password_id, operation, user_name)
        return result