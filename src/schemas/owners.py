from pydantic import BaseModel
from pydantic.types import PaymentCardNumber


class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: str