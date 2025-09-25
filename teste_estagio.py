from random import randint


def return_odd_number():
    """Return a odd number between 0 and a hundred thousand"""
    number = randint(0, 100000)
    while number % 2 == 0:
        number = randint(0, 100000)
    return number

def return_even_number():
    """Return a even number between 0 and a hundred thousand"""
    number = randint(0, 100000)
    while number % 2 != 0:
        number = randint(0, 100000)
    return number

def return_text():
    """Return a default text"""
    text = "Hello World!"
    return text

