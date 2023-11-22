# NIM 351

def title_decorator(function):
    def wrapper():
        func = function()
        make_title = func.title()
        print(make_title + " " + "-Data is convert to title case")
        return make_title
    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        print(str(splitted_string)+ "" + "- Then  data is splitted") 
        return splitted_string
    return wrapper


# dekorator title dan split string
@split_string
@title_decorator
def say_hi():
    return 'Hello there'

decorated_say_hi = say_hi()