from src.fizz_buzz import fizz_buzz


def test_fizz_buzz_3_returns_fizz():
    assert fizz_buzz(3) == "Fizz"

def test_fizz_buzz_5_returns_buzz():
    assert fizz_buzz(5) == "Buzz"

def test_fizz_buzz_6_returns_fizz():
    assert fizz_buzz(6) == "Fizz"

def test_fizz_buzz_0_returns_str_0():
    assert fizz_buzz(0) == "0"

def test_fizz_buzz_1_returns_str_1():
    assert fizz_buzz(1) == "1"

def test_fizz_buzz_2_returns_str_2():
    assert fizz_buzz(2) == "2"

def test_fizz_buzz_15_returns_fizzbuzz():
    assert fizz_buzz(15) == "FizzBuzz"