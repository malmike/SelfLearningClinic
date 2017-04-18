def generatePrimeNumbers(num):
    numbers_types = (int, float, complex)
    if isinstance(num, numbers_types):
        pass
    else:
        raise TypeError