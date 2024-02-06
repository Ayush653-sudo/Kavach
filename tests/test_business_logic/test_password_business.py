"""
This module is to perform unit testing of password business class.
"""

from unittest import mock
import pytest
from cryptography.fernet import Fernet
from src.business_logic.password_business import PasswordBusiness
from src.helpers.exceptions.not_found import NotFoundError
from src.helpers.exceptions.range_error import RangeError
from src.models.password import Password


fernet = Fernet.generate_key()
fernet_obj = Fernet(fernet)

class TestPasswordBusiness:
    password_business = PasswordBusiness()
    generated_key = Fernet.generate_key()
    
    @mock.patch("src.business_logic.password_business.check_strength",return_value=["Your Password should contain at least one number"])
    def test_check_password_strength(self,strength_checker):
        actual = self.password_business.check_password_strength("Ayush#")
        expected = ["Your Password should contain at least one number"]
        assert len(actual) == len(expected)
        for i in range(len(actual)):
            assert actual[i] == expected[i]

    @mock.patch("src.business_logic.password_business.random.choice",side_effect=['4','A','l','#','4','A','l','#'])
    def test_generate_password_validlength_return_password(self,mock_choice):
        length = 8
        actual = self.password_business.generate_password(length)
        expected = "4Al#4Al#"
        assert actual == expected
        assert mock_choice.call_count == length
    
    @mock.patch("src.business_logic.password_business.RangeError",return_value = RangeError("You must enter length grater than or equal to 8"))
    def test_generate_password_invalidlength_throwrangeerror(self,mock_range_error):
        with pytest.raises(RangeError) as exc:
            self.password_business.generate_password(4)
        assert exc.type == RangeError
        assert exc.value.message == "You must enter length grater than or equal to 8"

    @mock.patch("src.business_logic.password_business.db.fetch_data_from_database",return_value = [("ayush",Fernet.generate_key())])
    @mock.patch("src.business_logic.password_business.db.add_data_to_database")
    @mock.patch("src.business_logic.password_business.Fernet",return_value = Fernet(Fernet.generate_key()))
    def test_add_password_valid_password_object(self, mock_fetch_data, mock_add_data,mock_fernet):
        self.password_business.add_password(Password("ayush","www.google.com","yahoo","login"))
        mock_add_data.assert_called_once()
        mock_fetch_data.assert_called_once()
        mock_fernet.assert_called_once()

   
    @mock.patch("src.business_logic.password_business.db.fetch_data_from_database",return_value = [("test_password_id","ayush","www.google.com","login")])
    def test_get_password_by_username(self,fetched_data_from_database):
        actual = self.password_business.get_password_by_username("ayush")
        expected = [("test_password_id","ayush","www.google.com","login")]
        assert len(actual) == len(expected)
        for i in range(len(actual)):
            assert actual[i] == expected[i]
        
    @mock.patch("src.business_logic.password_business.db.fetch_data_from_database",return_value=[(fernet_obj.encrypt("Ayush#199".encode()),fernet)])
    @mock.patch("src.business_logic.password_business.Fernet",return_value = fernet_obj)
    def test_get_decrypted_password(self,mock_fetch_data,mock_fetnet):
         expected = [("Mypassword_test_id","Ayush#199")]
         actual = self.password_business.get_decrypted_password("Mypassword_test_id","ayush")
         mock_fetch_data.assert_called_once()
         mock_fetnet.assert_called_once()
         assert expected == actual
    

    @mock.patch("src.business_logic.password_business.db.fetch_data_from_database",return_value=[])
    @mock.patch("src.business_logic.password_business.Fernet",return_value = fernet_obj)
    @mock.patch("src.business_logic.password_business.NotFoundError",return_value=NotFoundError("Sorry no data found!!!!"))
    def test_get_decrypted_password(self,mock_fetch_data,mock_fetnet,mock_not_found):
        
         with pytest.raises(NotFoundError) as exc: 
            self.password_business.get_decrypted_password("Mypassword_test_id","ayush")
         mock_fetch_data.assert_called_once()
         assert exc.type == NotFoundError
         assert exc.value.message == "Sorry no data found!!!!"
         
    @mock.patch("src.business_logic.password_business.db.fetch_data_from_database",side_effect = [[("ayush",fernet)],[("test_password_id","ayush","www.google.com","login")]])
    @mock.patch("src.business_logic.password_business.db.add_data_to_database")
    @mock.patch("src.business_logic.password_business.Fernet",return_value = fernet_obj)
    def test_updated_password_valid_id(self,mock_fetch_data, mock_add_data, mock_fernet):
        actual = self.password_business.update_password("test_password_id","ayush","Aysuh#18")
        mock_add_data.assert_called_once()
        mock_fernet.call_count == 2
        mock_fetch_data.call_count == 2

    @mock.patch("src.business_logic.password_business.db.fetch_data_from_database",side_effect = [[("ayush",fernet)],[("test_password_id","ayush","www.google.com","login")]])
    @mock.patch("src.business_logic.password_business.db.add_data_to_database")
    @mock.patch("src.business_logic.password_business.Fernet",return_value = fernet_obj)
    @mock.patch("src.business_logic.password_business.NotFoundError",return_value=NotFoundError("Sorry no data found!!!!"))
    def test_updated_password_invalid_id(self,mock_fetch_data, mock_add_data, mock_fernet,not_found_error):

        with pytest.raises(NotFoundError)as exc:
             self.password_business.update_password("wrong_password_id","ayush","Aysuh#18")
        assert exc.type == NotFoundError
        assert exc.value.message == "Sorry no data found!!!!"
        mock_fernet.call_count == 2
        mock_fetch_data.call_count == 2
     
    @mock.patch("src.business_logic.password_business.db.fetch_data_from_database",return_value = [("test_password_id","ayush","www.google.com","login")])
    @mock.patch("src.business_logic.password_business.db.add_data_to_database")
    def test_delete_pssword_validpassword_id(self,mock_fetch_data,mock_add_data):
        self.password_business.delete_password("test_password_id","ayush")
        mock_add_data.assert_called_once()
        mock_fetch_data.assert_called_once()
    
    @mock.patch("src.business_logic.password_business.db.fetch_data_from_database",return_value = [("test_password_id","ayush","www.google.com","login")])
    @mock.patch("src.business_logic.password_business.db.add_data_to_database")
    @mock.patch("src.business_logic.password_business.NotFoundError",return_value=NotFoundError("Sorry no data found!!!!"))
    def test_delete_pssword_invalidpassword_id(self,mock_fetch_data,mock_add_data,notfounderror):
        
        with pytest.raises(NotFoundError)as exc:
            self.password_business.delete_password("test_password","ayush")
        assert exc.type == NotFoundError
        assert exc.value.message == "Sorry no data found!!!!"
        mock_fetch_data.assert_called_once()
        
    


    


    
    

    