def data_type(arg):
    #Check that the argument passed is a list
    if isinstance(arg, list):
        #If the list has more than 2 values return the 3rd value 
        #Else return None
        if len(arg) > 2:
            return arg[2]
        else:
            return None
    #Check that the argument is a bool, if so return its value
    elif isinstance(arg, bool):
        return arg
    #Check that the argument is a number
    elif isinstance(arg, int):
        if arg < 100:
            return 'less than 100'
        elif arg == 100:
            return 'equal than 100'
        else:
            return 'more than 100'
    #Check that the argument is a string, if so return its length
    elif isinstance(arg, str):
        return len(arg)
    #Check that no argument is passed
    elif arg is None:
        return 'no value'