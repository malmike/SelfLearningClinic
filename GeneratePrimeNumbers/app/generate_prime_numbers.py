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
            #Set loop to get prime numbers less than num
            while nextPrime < num:
                #Set bool isPrime to True
                isPrime = True
                #Get the square root of nextPrime
                sqrt_value = sqrt(nextPrime)
                #Select values in prime_list that are less than sqrt_value and put them in a list sample_range
                sample_range = [i for i in prime_list if i <= sqrt_value]
                #Loop through the sample_range values
                for i in sample_range:
                    #Test that the value nextPrime is not divisible by the values in sample_range
                    if nextPrime%i == 0:
                        #If the value is divisible set isPrime to false and break out of the loop
                        isPrime = False
                        break
                #If isPrime is still set to true then add value to prime_list
                if isPrime:
                    prime_list.append(nextPrime)
                nextPrime += 2
            #Return prime_list        
            return prime_list
        else:
            raise ValueError
    else:
        raise TypeError
