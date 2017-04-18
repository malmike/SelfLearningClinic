def fizz_buzz(arg):
    value = ''
    divisible = False
    if arg % 3 == 0:
        divisible = True
        value += 'Fizz'
    if arg % 5 == 0:
        divisible = True
        value += 'Buzz'
    if divisible:
        return value
    else:
        return arg