import datetime


limit_time = datetime.timedelta(0,10,0,0,0,0,0)
def time_control(func):
    def wrapper(*args,**kwargs):
        global limit_time
        start_time = datetime.datetime.now()
        result = func(*args,**kwargs)
        finish_time = datetime.datetime.now()
        if (finish_time - start_time) < limit_time:
            return result
        else:
            raise Error("Error! The duration of the program is more than 10 seconds.")
    return wrapper

@time_control
def summ(*args,**kwargs):
    total = 0
    for arg in args:
        total = total + arg
    for key in kwargs:
        total = total + kwargs[key]
    return total
