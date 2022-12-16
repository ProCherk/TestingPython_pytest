from enum import Enum
from src.baseclasses.pyenum import PyEnum


class Genders(Enum):
    FEMALE = "female"
    MALE = "male"


class Status(PyEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class UserStatus(PyEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn't contain @"
