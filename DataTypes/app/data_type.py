def data_type(arg):
    
    if isinstance(arg, list):
        if len(arg) > 2:
            return arg[2]
        else:
            return None
    elif isinstance(arg, bool):
        return arg
    elif isinstance(arg, int):
        if arg < 100:
            return 'less than 100'
        elif arg == 100:
            return 'equal than 100'
        else:
            return 'more than 100'
    elif isinstance(arg, str):
        return len(arg)
    elif arg is None:
        return 'no value'