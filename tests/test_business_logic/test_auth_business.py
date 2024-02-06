"""
This module is only to test methods of AuthBusiness class

"""
import hashlib
from unittest import mock
import pytest
from src.business_logic.auth_business import AuthBusiness
from src.config.query import QueryConfig
from src.helpers.exceptions.not_found import NotFoundError
from src.models.users import User


class TestAuthBusiness:
    """
    This is class which is used for testing AuthBusiness class functions
    """
    mock_user = User("ayush","4fe89e0893233a387e3133a8609e9b0a95b3b0acec3124b44cfeb50d1da657e9","9636653732","ayushsinght70@gmail.com","Admin","active")
    mock_user_2 = User("akshat","Ayush#18","9636653732","ayushsinght70@gmail.com","Admin","active")
    auth_business = AuthBusiness()
    
    @mock.patch("src.business_logic.auth_business.db.fetch_data_from_database",return_value=[("ayush","Ayush#18","9636653732","ayushsinght70@gmail.com","Admin","active")])
    @mock.patch("src.business_logic.auth_business.hashlib.sha256",return_value=hashlib.sha256("ayush#18".encode('utf-8')))
    @mock.patch("src.business_logic.auth_business.Fernet.generate_key",return_value=bytes("keyeee".encode()))
    @mock.patch("src.business_logic.auth_business.db.add_data_to_database")
    def test_register_user_to_db(self,mock_data_base, sha256, generate_key, fetch_data_from_database,):
        
        self.auth_business.register_user_to_db(self.mock_user_2)
        sha256.assert_called_once()
        generate_key.assert_called_once()
        fetch_data_from_database.assert_called_once()
        assert mock_data_base.call_count,2
    
    @mock.patch("src.business_logic.auth_business.db.fetch_data_from_database",return_value=[("ayush","4fe89e0893233a387e3133a8609e9b0a95b3b0acec3124b44cfeb50d1da657e9","9636653732","ayushsinght70@gmail.com","Admin","active")])
    @mock.patch("src.business_logic.auth_business.hashlib.sha256",return_value=hashlib.sha256("Ayush#18".encode('utf-8')))
    def test_get_user_by_username_and_password(self,sha256,fetch_data_from_database):
       user = self.auth_business.get_user_by_username_and_password(("ayush","Ayush#18"))
       assert user.username == self.mock_user.username
       sha256.assert_called_once()
       fetch_data_from_database.assert_called_once()
    

    @mock.patch("src.business_logic.auth_business.db.fetch_data_from_database",return_value=[("lyush","4fe89e0893233a387e3133a8609e9b0a95b3b0acec3124b44cfeb50d1da657e9","9636653732","ayushsinght70@gmail.com","Admin","active")])
    @mock.patch("src.business_logic.auth_business.hashlib.sha256",return_value=hashlib.sha256("Ayush#18".encode('utf-8')))
    @mock.patch("src.business_logic.auth_business.NotFoundError",return_value=NotFoundError("Sorry no data found!!!!"))
    def test_get_user_by_username_and_password_Invalidusername_raise_notfounderror(self,fetch_data_from_database,notfond,sha256):
        with pytest.raises(NotFoundError) as exc:
            self.auth_business.get_user_by_username_and_password(("ayush","Ayush#18"))
        assert exc.type == NotFoundError
        assert exc.value.message == "Sorry no data found!!!!"
        sha256.assert_called_once()
        fetch_data_from_database.assert_called_once()
        notfond.assert_called_once()


               
               
  






        




