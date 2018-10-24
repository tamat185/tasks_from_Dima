def amount_call_func(func):
    total = 0
    def wrapper(*args, **kwargs):
        nonlocal total
        total = total + 1
        return func(*args, **kwargs)
    return wrapper

@amount_call_func
def summ(*args, **kwargs):
    total = 0
    for arg in args:
        total = total + arg
    for key in kwargs:
        total = total + kwargs[key]
    return total
