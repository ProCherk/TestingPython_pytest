import pytest
from src.baseclasses.response import Response
from src.schemas.user import User
from src.enums.user_enums import Status, UserStatus
from src.schemas.computer import Computer
from example import computer


@pytest.mark.api_test  # for start test with markers in terminal needed parameter "-k _name of marker_"
def test_getting_users_list(get_users):  # in () name of fixture
    test_obj = Response(get_users)
    test_obj.assert_status_code(200).validate(User)


@pytest.mark.api_test
@pytest.mark.parametrize("status", Status.list())
def test_generator(status, get_player_generator):  # test generated data
    print(get_player_generator.set_status(status=status).build())


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


@pytest.mark.api_test
def test_computer():
    comp = Computer.parse_obj(computer)
    print(comp.detailed_info.owners)
