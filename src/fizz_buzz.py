def fizz_buzz(number):
    result = ""
    if number == 0:
        return "0"
    if number % 3 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += "Buzz"
    return result or str(number)