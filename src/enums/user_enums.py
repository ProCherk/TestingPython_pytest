from enum import Enum


class Genders(Enum):
    FEMALE = "female"
    MALE = "male"


class Status(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn't contain @"
