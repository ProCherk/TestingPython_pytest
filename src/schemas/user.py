from pydantic import BaseModel, validator
from src.enums.user_enums import Genders, Status, UserErrors


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders
    status: Status

    @validator('email')
    def check_email_include_ad_symbol(cls, em):
        if "@" in em:
            return em
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)



