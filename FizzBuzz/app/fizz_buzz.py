def fizz_buzz(arg):
    numbers_types = (int, float, complex)
    #Check that the argument passed is a number
    if isinstance(arg, numbers_types):
        #Initialise a variable value that will hold Fizz &/or Buzz
        #Initialise a boolean used to show that Fizz &/or Buzz have been set
        value = ''
        divisible = False
        #Check whether the argument is divisible by 3, if so add Fizz to value and set divisible to True
        if arg % 3 == 0:
            divisible = True
            value += 'Fizz'
        #Check whether the argument is divisible by 5, if so add Buzz to value and set divisible to True
        if arg % 5 == 0:
            divisible = True
            value += 'Buzz'
        #Check whether divisible is true, if so return value else return the argument passed
        if divisible:
            return value
        else:
            return arg
    else:
        return arg