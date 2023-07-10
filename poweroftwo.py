from math import log2

try:
    number = int(input('Enter your number: '))
except ValueError as err:
    print(err)
    exit()

def is_power_of_two(n:int)->int:
    if log2(n).is_integer():
        return True
    return False



print(is_power_of_two(number))