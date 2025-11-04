from src.fizz_buzz import fizz_buzz
import pytest

@pytest.mark.parametrize("number,expected_result",[
    (0, "0"),
    (1, "1"),
    (2, "2"),
    (3, "Fizz"),
    (4, "4"),
    (5, "Buzz"),
    (6, "Fizz"),
    (10, "Buzz"),
    (15, "FizzBuzz"),
    (30, "FizzBuzz"),
])
def test_fizz_buzz_number_returns_expected_result(number, expected_result):
    assert fizz_buzz(number) == expected_result