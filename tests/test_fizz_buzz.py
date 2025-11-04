from src.fizz_buzz import fizz_buzz


def test_fizz_buzz_3_returns_fizz():
    assert fizz_buzz(3) == "Fizz"

def test_fizz_buzz_5_returns_buzz():
    assert fizz_buzz(5) == "Buzz"