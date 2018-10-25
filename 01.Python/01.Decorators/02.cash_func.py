def cash (func):
    cash_list = {}
    def wrapper(*args,**kwargs):
        nonlocal cash_list
        if (tuple(args) + tuple(kwargs.values())) in cash_list:
            return cash_list[(tuple(args) + tuple(kwargs.values()))]
        else:
            result_func = func(*args,**kwargs)
            cash_list[(tuple(args) + tuple(kwargs.values()))] = result_func
            return result_func
    return wrapper

@cash
def suma(*args, **kwargs):
    total = 0
    for arg in args:
        total = total + arg
    for key in kwargs:
        total = total + kwargs[key]
    return total

suma(1,2)
suma(1,3)
suma(1,2)
suma(1,4)
suma(1,a=4)
