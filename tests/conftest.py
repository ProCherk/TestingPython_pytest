import pytest
import random
from src.generators.player import Player


@pytest.fixture  # smth that will execute before the test
def get_number():
    return random.randint(0, 100)


def _calculate(a, b):  # need to return method like object, not a result
    return a+b


@pytest.fixture  # fixture to return method
def calculate():
    return _calculate


@pytest.fixture
def make_number():
    print("im getting number")
    number = random.randrange(1, 1000, 5)
    yield number  # like return but after execution "yield" fixture continue to work
    print(f"fixture need to be closed, result number {number}")


@pytest.fixture
def get_player_generator():
    return Player()
