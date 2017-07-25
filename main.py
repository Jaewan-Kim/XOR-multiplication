import math


def toBinary(number):
    if math.floor(number/2) != 0:
        return toBinary(math.floor(number/2)) + str(number%2)
    return str(number%2)


def XORaddition(number1, number2):
    digit = 1