class Subject:
    def request(self):
        pass

class Realsub(Subject):
    def request(self):
        print("Real subject is called.")
class Proxy:
    def __init__(self,realsub):
        self.realsub=realsub
    def request(self):
        print("Running Addition functions by Proxy")
        self.realsub.request()

#client code
if __name__=="__main__":
    realsubject=Realsub()
    proxyz=Proxy(realsubject)

    proxyz.request()
