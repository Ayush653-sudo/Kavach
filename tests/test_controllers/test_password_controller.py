from unittest import mock
import pytest
from src.config.app_config import AppConfig
from src.config.prompts.prompts import Prompts

from src.controllers.password_controller import PasswordController
from src.models.audit_password import AuditPassword
from src.models.password import Password

Prompts.load()
class TestPasswordController:
    
    password_obj = Password("ayush","www.google.com","Ayush@12","login")
    @pytest.fixture(autouse=True)
    def mock_password_business(self):
        self.obj = PasswordController(mock.MagicMock(),mock.MagicMock())
    
    
    def test_check_password_returnlist(self):
        self.obj.password_business.check_password_strength.return_value = ["Your Password is strong enough"]
        actual = self.obj.check_password("Ayush@12")
        expected = ["Your Password is strong enough"]
        assert len(actual) == len(expected)
        assert actual == expected
        self.obj.password_business.check_password_strength.assert_called_once() 
     
    def test_generate_password_returnstring(self):
        self.obj.password_business.generate_password.return_value = "Aysuh@1233"
        actual = self.obj.generate_password(10)
        expected = "Aysuh@1233"
        assert expected == actual
        self.obj.password_business.generate_password.assert_called_once()


    
    def test_add_new_password_returnstring(self):
        self.obj.password_business.add_password.return_value = None
        self.obj.audit_business.add_audit_password.return_value = None
        actual = self.obj.add_new_password(self.password_obj)
        expected = Prompts.PASSWORD_ADDED_SUCCESSFULLY
        assert actual == expected
        self.obj.password_business.add_password.assert_called_once()
        self.obj.audit_business.add_audit_password.assert_called_once()
        
    def test_get_passwords_by_username_returnlistofpasswords(self):
        self.obj.password_business.get_password_by_username.return_value = [self.password_obj]
        actual = self.obj.get_passwords_by_username("ayush")
        expected = [self.password_obj]
        assert actual == expected
        self.obj.password_business.get_password_by_username.assert_called_once()

    def test_get_decrypted_password_by_id_retrunstring(self):
        self.obj.password_business.get_decrypted_password.return_value = "aysuhS@12"
        self.obj.audit_business.add_audit_password.return_value = None
        actual = self.obj.get_decrypted_password_by_id("testpasswordid","ayush")
        expected = "aysuhS@12"
        assert expected == actual
        self.obj.password_business.get_decrypted_password.assert_called_once()
        self.obj.audit_business.add_audit_password.assert_called_once()
    
     
    def test_updated_password_returnstring(self):
         self.obj.password_business.update_password.return_value = None
         self.obj.audit_business.add_audit_password.return_value = None
         actual = self.obj.update_password("testpassword_id","ayush","Ayush#118")
         expected = "PASSWORD UPDATED SUCESSFULLY"
         assert actual == expected
         self.obj.password_business.update_password.assert_called_once()
         self.obj.audit_business.add_audit_password.assert_called_once()
     
    def test_delete_password_by_id_returnstring(self):
        self.obj.password_business.delete_password.return_value = None
        actual = self.obj.delete_password_by_id("testpasswordid","ayush")
        expected = Prompts.PASSWORD_DELETED_SUCCESSFULLY
        assert actual == expected
        self.obj.password_business.delete_password.assert_called_once()


         

