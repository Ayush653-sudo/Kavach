from unittest import mock

import pytest
from src.business_logic.audit_business import AuditBusiness
from src.models.audit_password import AuditPassword

class TestAuditBusiness:
    """
    This class will test methods of audit business
    """
    audit_password = AuditPassword("22","Fetched","Ayush")
    
    
    @mock.patch("src.business_logic.audit_business.db.add_data_to_database")
    def test_add_audit_password(self, add_data_to_database):
        obj = AuditBusiness()
        obj.add_audit_password(AuditPassword("22","Fetched","Ayush"))
        add_data_to_database.assert_called_once()
    
    @mock.patch("src.business_logic.audit_business.db.fetch_data_from_database",return_value=[("dd","dd","dkdvm","kvmdskvn")] )
    def test_get_password_audit_by_status_from_db(self,fetch_data_from_database):
        obj = AuditBusiness()
        actual = obj.get_password_audit_by_status_from_db("dd","dd","dkdvm")
        fetch_data_from_database.assert_called_once()
        expected = [("dd","dd","dkdvm","kvmdskvn")]
        assert actual == expected
        fetch_data_from_database.assert_called_once()
        
    

    

        
        
    



    
