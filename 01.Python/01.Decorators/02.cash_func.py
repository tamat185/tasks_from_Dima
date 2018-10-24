def cash (func):
    cash_list = {}
    def wrapper(*args):
        nonlocal cash_list
        if args in cash_list.keys():
            print(cash_list)
            return cash_list[args]
        else:
            result_func = func(*args)
            cash_list[args] = result_func
            print(cash_list)
            return result_func
    return wrapper

@cash
def suma(*args):
    total = 0
    for arg in args:
        total = total + arg
    return total

suma(1,2)
suma(1,3)
suma(1,2)
