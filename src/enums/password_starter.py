from enum import Enum


class PasswordStarter(Enum):
    AddPassword = "1"
    WatchPassword = "2"
    UpdatePassword = "3"
    DeletePassword = "4"
    CheckPasswordAudits = "5"
    GOBACK = "6"
