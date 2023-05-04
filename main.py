def log_call(func):
    def wrapper(*args, **kwargs):
        returning = func(*args, **kwargs)
        print(f'function {func.__name__}, recieve arguments args{args}, and kwargs{kwargs}, and return{returning}')
        return returning
    return wrapper

@log_call
def temperature(C):
    return C*1.8+32
print(temperature(32))
print(temperature(40))
print(temperature(50))