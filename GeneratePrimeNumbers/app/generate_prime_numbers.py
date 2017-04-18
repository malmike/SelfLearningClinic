import math

def generatePrimeNumbers(num):
    numbers_types = (int, float, complex)
    #Check that the value inserted is a number
    if isinstance(num, numbers_types):
        #Check that the value inserted is greater than or equal to 3
        if num >= 3:
            pass
        else:
            raise ValueError
    else:
        raise TypeError