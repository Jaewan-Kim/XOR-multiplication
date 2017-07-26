import math


def toBinary(number):
    if math.floor(number/2) != 0:
        return toBinary(math.floor(number/2)) + str(number%2)
    return str(number%2)


def XORMultiplication(number1, number2):
    number = int(number1) * int(number2)
    output = ''
    for chr in str(number):
        if int(chr) % 2 == 0:
            output += '0'
        else:
            output += '1'
    return output


input1 = int(input('enter the first number: '))
input2 = int(input('enter the second number: '))

print(XORMultiplication(toBinary(input1),toBinary(input2)))
