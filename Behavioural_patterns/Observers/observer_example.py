class Observer:
    def update(self,message):
        pass

class ConcreteObserver(Observer):
    def __init__(self,name):
        self.name=name
    def update(self,message):
        print(f"{self.name} received message:{message}")

class Subject:
    def __init__(self):
        self._observers=[]
    def add_observer(self,observer):
        self._observers.append(observer)
    def remove_observer(self,observer):
        self._observers.remove(observer)
    def notify_observer(self,message):
        for observer in self._observers:
            observer.update(message)
    def perform_action(self,action):
        print(f"Performing action:{action}")
        self.notify_observer(f"Action={action}")

observer1=ConcreteObserver("Observer1")
observer2=ConcreteObserver("Observer2")
subject=Subject()
subject.add_observer(observer1)
subject.add_observer(observer2)
subject.perform_action("Update1")
subject.perform_action("Update2")
