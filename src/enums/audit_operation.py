from enum import Enum


class AuditOperation(Enum):
    FETCHED = "1"
    ADDED = "2"
    UPDATED = "3"
    GOBACK = "4"