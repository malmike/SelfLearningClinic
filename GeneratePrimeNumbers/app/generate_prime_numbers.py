from math import sqrt

def generatePrimeNumbers(num):
    numbers_types = (int, float, complex)
    #Check that the value inserted is a number
    if isinstance(num, numbers_types):
        #Check that the value inserted is greater than or equal to 3
        if num >= 3:
            #List to hold the prime numbers
            prime_list = []
            #Added initial prime number 2
            prime_list.append(2)
            nextPrime = 3
        
            #Return prime_list        
            return prime_list
        else:
            raise ValueError
    else:
        raise TypeError
