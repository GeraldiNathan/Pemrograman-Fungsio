def uppercase_decorator(function):
    def wrapper():
        funct = function()
        return funct.upper()
    return wrapper

@uppercase_decorator
def say_hi():
    return 'Hello there'

decorated_say_hi = say_hi()
print(decorated_say_hi)