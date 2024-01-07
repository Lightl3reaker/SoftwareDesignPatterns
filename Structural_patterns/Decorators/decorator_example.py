def my_deco(func):
    def wrapper():
        print("Actions before function call")
        func()
        print("Actions after function call")
    return wrapper

@my_deco
def say_hi():
    print("Hi i am a function.")

say_hi()
