
from unittest import mock
import pytest
from src.business_logic.audit_business import AuditBusiness

from src.controllers.audit_controller import AuditController

class TestAuditController:
    """
    This class perform testing all methods present in AuditController class
    """
    mock_data = [("dd","dd","dkdvm","kvmdskvn")]
    @pytest.fixture(autouse=True)
    def mock_audit_business(self):
        self.obj = AuditController(mock.MagicMock())
        # print(self.obj)
    
    def test_get_password_fetched_audit(self):
        self.obj.audit_business.get_password_audit_by_status_from_db.return_value = self.mock_data
        actual = self.obj.get_password_fetched_audit("Test_password_id","Fetched","ayush")
        assert actual == self.mock_data
        self.obj.audit_business.get_password_audit_by_status_from_db.assert_called_once()

    
    


