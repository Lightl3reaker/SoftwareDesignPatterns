#Making a logger for function cals
class Logger:
    def __init__(self,func):
        self.func=func
    def __call__(self,*args,**kwargs):
        print(f"Calling {self.func.__name__} with arguments:{args} and keyword args:{kwargs}")
        result=self.func(*args,**kwargs)
        print(f"{self.func.__name__} returned {result}")

@Logger
def adder(a,b):
    return a+b
@Logger
def substractor(a,b):
    return a-b

adder(3,2)
substractor(6,3)
