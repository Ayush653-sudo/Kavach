from datetime import datetime
import uuid

class AuditPassword:
    def __init__(self,password_id, operation,user_name,datetime = datetime.now()) -> None:
        self.id = str(uuid.uuid1())
        self.password_id = password_id
        self.operation = operation
        self.user_name = user_name
        self.datetime = datetime
        
        
    