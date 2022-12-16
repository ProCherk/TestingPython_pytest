from pydantic import BaseModel
from pydantic.types import PastDate, FutureDate
from pydantic.networks import IPv4Network, IPv6Network
from src.enums.user_enums import Status
from example import computer
from src.schemas.detailed_info import DetailedInfo


class Computer(BaseModel):
    id: int
    status: Status
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Network
    host_v6: IPv6Network
    detailed_info: DetailedInfo

 # comp = Computer.parse_obj(computer)
 #
 # print(comp)


