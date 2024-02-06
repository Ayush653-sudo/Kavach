from unittest import mock
import pytest

from src.business_logic.users_business import UserBusiness
from src.helpers.exceptions.not_found import NotFoundError


class TestUserPassword:
    """
    This class is used to test the method of UserBusiness class.
    """
    users_business = UserBusiness()
    @mock.patch("src.business_logic.users_business.db.fetch_data_from_database",return_value =[("ayush","9636653732","ayushsinght70@gmail.com","Admin","active")])
    def test_get_all_users(self,mock_fetch_data):
        expected = [("ayush","9636653732","ayushsinght70@gmail.com","Admin","active")]
        actual = self.users_business.get_all_users()
        assert actual == expected

    @mock.patch("src.business_logic.users_business.db.fetch_data_from_database",return_value =[("ayush","9636653732","ayushsinght70@gmail.com","Admin","active")])
    @mock.patch("src.business_logic.users_business.db.add_data_to_database")
    def test_inactive_user_valid_username(self, mock_fetch_data, mock_add_data):
        self.users_business.inactive_user("ayush")
        mock_add_data.assert_called_once()
        mock_fetch_data.assert_called_once()

    
    @mock.patch("src.business_logic.users_business.db.fetch_data_from_database",return_value =[("ayush","9636653732","ayushsinght70@gmail.com","Admin","active")])
    @mock.patch("src.business_logic.users_business.db.add_data_to_database")
    @mock.patch("src.business_logic.users_business.NotFoundError",return_value=NotFoundError("Sorry no data found!!!!"))
    def test_inactive_user_invalid_username(self, mock_fetch_data, mock_add_data,mock_Error_obj):
        
        with pytest.raises(NotFoundError) as exc: 
            self.users_business.inactive_user("ayushi")
        mock_fetch_data.assert_called_once()
        mock_Error_obj.assert_called_once()
        assert exc.type == NotFoundError
        assert exc.value.message == "Sorry no data found!!!!"
        
