class Target:
    def request(self):
        pass

class Adaptee:
    def specific_req(self):
        print("This is from adaptee.")

class Adapter(Target):
    def __init__(self,adaptee):
        self.adaptee=adaptee
    def request(self):
        print("Using Adapter")
        self.adaptee.specific_req()
def client_code(target):
    target.request()


adaptee=Adaptee()
adapter=Adapter(adaptee)
client_code(adapter)

