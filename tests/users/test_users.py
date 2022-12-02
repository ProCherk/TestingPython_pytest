import pytest
import requests
from src.baseclasses.response import Response
from configuration import SERVICE_URL
from src.schemas.user import User


# resp = requests.get(SERVICE_URL)
# print(resp.url)
# a = resp.json()
# print(a)

@pytest.mark.api_test  # for start test with markers in terminal needed parameter "-k _name of marker_"
def test_getting_users_list(get_users):  # in () name of fixture
    test_obj = Response(get_users)
    test_obj.assert_status_code(200).validate(User)


@pytest.mark.func_test
@pytest.mark.skip("Why it skipped")  # how to skip tests
def test_assert():
    assert 1 == 1


@pytest.mark.func_test
@pytest.mark.parametrize("first_value, second_value, result", [  # how to test 1 function in 1 test using many values
    (1, 2, 3),
    (-1, 2, 1),
    (-1, -2, -3)
])
def test_calculator(first_value, second_value, result, calculate):
    assert calculate(first_value, second_value) == result

