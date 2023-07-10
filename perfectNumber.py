from math import pow

try:
    number = int(input('Enter your number: '))
except ValueError as err:
    print(err)
    exit()

def perfect_number(k:int)->int:
     return int(pow(2,k-1)*(pow(2,k)-1))

def is_perfect_number(n:int)->bool:
        k = 1
        while True:
            if perfect_number(k) == n:
                return True
            elif perfect_number(k)> n:
                return False
            k += 1
             

             
print(is_perfect_number(number))

