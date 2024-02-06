"""
This module is developed ony for auditing purpose.
"""
from models.audit_password import AuditPassword
from database_layer.database import db
from config.query import QueryConfig


class AuditBusiness:
    """
    This class deals with auditing and calling db to commit the audit. 
    """
    def add_audit_password(self, audit_password: AuditPassword):     
        db.add_data_to_database(QueryConfig.INSERT_AUDIT_PASSWORD_INTO_TABLE, (audit_password.id, audit_password.password_id, audit_password.operation, audit_password.datetime,audit_password.user_name))
     
    def get_password_audit_by_status_from_db(self, password_id: str, status:str ,user_name:str) -> list:
       r =  db.fetch_data_from_database(QueryConfig.GET_AUDIT,(password_id,status,user_name))
       return r
        

