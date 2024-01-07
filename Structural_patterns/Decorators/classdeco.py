#using class as decorator
class deco:
    def __init__(self,func):
        self.func=func
    def __call__(self):
        print("Actions before function call.")
        self.func()
        print("Actions after function call.")
@deco
def greeting():
    print("Hi How are you.")

greeting()

