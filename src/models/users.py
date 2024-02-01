

class User:
    def __init__(self, username, password, phone_number, email_address, role, status="active"):
        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.email_address = email_address
        self.role = role
        self.status = status

