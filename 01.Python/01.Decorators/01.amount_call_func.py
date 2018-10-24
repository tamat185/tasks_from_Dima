
def amount_call_func(func):
    total = 0
    def wrapper(*args):
        nonlocal total
        total = total + 1
        print(total)
        func(*args)
    return wrapper

@amount_call_func
def summ(a, b):
    return a + b

@amount_call_func
def div(a, b):
    return a - b

summ(1,3)
div(1,7)
summ(4, 78)
div(5, 78)
