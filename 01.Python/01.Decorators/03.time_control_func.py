import datetime


limit_time = datetime.timedelta(0,10,0,0,0,0,0)
def time_control(func):
    def wrapper(*args):
        global limit_time
        start_time = datetime.datetime.now()
        result = func(*args)
        finish_time = datetime.datetime.now()
        if (finish_time - start_time) < limit_time:
            return result
        else:
            raise Error("Error! The duration of the program is more than 10 seconds.")
    return wrapper

@time_control
def summ(*args):
    total = 0
    for arg in args:
        total = total + arg
    return total

print(summ(1,2,3))
