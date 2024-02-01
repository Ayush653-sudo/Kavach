import pytest
from src.models.audit_password import AuditPassword
from cryptography.fernet import Fernet


@pytest.fixture
def dummy_audit_password():
    return AuditPassword("22","Fetched","Ayush")

@pytest.fixture
def dummy_fernet_key():
    return Fernet.generate_key()
@pytest.fixture
def dummy_fernet_obj():
    dummy_fernet_key = dummy_fernet_key()
    return Fernet(dummy_fernet_key)
