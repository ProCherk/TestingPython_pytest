import requests
from src.baseclasses.response import Response
from configuration import SERVICE_URL
from src.schemas.user import User


# resp = requests.get(SERVICE_URL)
# print(resp.url)
# a = resp.json()
# print(a)
#
def test_getting_users_list(get_users, make_number):  # in () name of fixture
    test_obj = Response(get_users)
    test_obj.assert_status_code(200).validate(User)

