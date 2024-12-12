import random

import pytest

from app.calculator import Calculator, CalculatorCache


def __random_numbers():
    return [random.randint(-100, 100) for _ in range(10)]


@pytest.fixture()
def calc():
    yield Calculator()


@pytest.fixture()
def calccache():
    yield CalculatorCache()


@pytest.fixture()
def input():
    yield [1, 2, 3, 4, 5]


@pytest.fixture()
def random_input():
    yield __random_numbers()


def test_addition(calc, input):
    result = calc.addition(input)
    assert result == 15


def test_multiplication(calc, input):
    result = calc.multiplication(input)
    assert result == 120


def test_multiplication_negative_6(calc):
    result = calc.multiplication([-6, -6])
    assert result > 0


def test_multiplication_negative_7(calc):
    result = calc.multiplication([-7, -7])
    assert result > 0


def test_addition_chaos(calc, random_input):
    # pytest . -v -s
    print(random_input)
    result = calc.addition(random_input)
    assert result == sum(random_input)


# Cannot use the fixture
@pytest.mark.parametrize("random_input", [__random_numbers() for _ in range(5)])
def test_addition_chaos_multiple_times(calc, random_input):
    print(random_input)
    result = calc.addition(random_input)
    assert result == sum(random_input)


@pytest.mark.parametrize("random_input", [__random_numbers() for _ in range(5)])
def test_addition_cache_chaos_multiple_times(calccache, random_input):
    print(random_input)
    result = calccache.addition(random_input)
    assert result == sum(random_input)


# This will fail
# @pytest.mark.failtest
# def test_addition_cache_chaos_multiple_times(calccache):
#     for random_input in [__random_numbers() for _ in range(5)]:
#         print(random_input)
#         result = calccache.addition(random_input)
#         assert result == sum(random_input)


def test_multiplication_min_error(calc):
    with pytest.raises(Exception) as exc_info:
        calc.multiplication([10])
