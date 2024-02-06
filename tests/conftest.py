import pytest
from src.helpers.exceptions.not_found import NotFoundError
from src.models.audit_password import AuditPassword
from cryptography.fernet import Fernet
from unittest import mock



@pytest.fixture
def dummy_audit_password():
    return AuditPassword("22","Fetched","Ayush")

@pytest.fixture
def mock_not_found(mocker):
    return mocker.patch("src.business_logic.users_business.NotFoundError",return_value=NotFoundError("Sorry no data found!!!!"))
    