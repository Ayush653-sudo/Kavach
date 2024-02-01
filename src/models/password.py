import datetime
import uuid
class Password:
    def __init__(self, user_name, website_url, password, password_type,
                 last_updated_date=datetime.datetime.now()):
        self.id = str(uuid.uuid1())
        self.user_name = user_name
        self.website_url = website_url
        self.password = password
        self.password_type = password_type
        self.last_updated = last_updated_date


