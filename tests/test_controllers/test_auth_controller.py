

from unittest import mock
import pytest
from src.config.prompts.prompts import Prompts
from src.controllers.auth_controller import AuthController
from src.helpers.error.error_response import ErrorResponse
from src.helpers.exceptions import dublicate_error
from src.models.users import User


class TestAuthController:
    
    @pytest.fixture(autouse=True)
    def mock_auth_business(self):
        self.obj = AuthController(mock.MagicMock())
     
    user = User("testuser","Test@13","9636653732","ayushsinght70@gmail.com","Admin")
    
    def test_register_user_valid_user(self):
       self.obj.auth_business.register_user_to_db.return_value = None
       actual= self.obj.register_user(self.user)
       assert actual == Prompts.USER_REGISTERED_SUCCESSFULLY
       self.obj.auth_business.register_user_to_db.assert_called_once()
    

    def test_register_user_dublicateError(self):
        self.obj.auth_business.register_user_to_db.side_effect = [dublicate_error.DuplicateError("user with same username found")]
        actual = self.obj.register_user(self.user)
        print(actual.message)
        
    
    def test_login_user(self):
         self.obj.auth_business.get_user_by_username_and_password.return_value = self.user
         actual =self.obj.login_user(("testuser","Test@123"))
         expected = self.user
         assert actual == expected
    
    def test_login_user_invalid_credential(self):
         self.obj.auth_business.get_user_by_username_and_password.return_value = None
         actual =self.obj.login_user(("testuser","Test@123"))
         expected = None
         assert actual == expected


    