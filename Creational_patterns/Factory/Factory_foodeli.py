# Let's consider a scenario where you are developing a system for an online food delivery service.
# The system has different types of restaurants, each offering a variety of dishes.
# Your task is to implement a system that allows the client code 
# to create instances of different restaurant objects
# without specifying their concrete classes, using the Factory Method design pattern.

from abc import ABC,abstractclassmethod

class Restaurant(ABC):
    @abstractclassmethod
    def create_dish(self,name,description,price):
        pass
class Dish(ABC):
    def __init__(self,name,description,price):
        self.name=name
        self.description=description
        self.price=price
    @abstractclassmethod
    def display(self):
        pass

class ItalianRestaurant(Restaurant):
    def create_dish(self,name,description,price):
        return ItalianDish(name,description,price)
class MexicanRestaurant(Restaurant):
    def create_dish(self,name,description,price):
        return MexicanDish(name,description,price)
class IndianRestaurant(Restaurant):
    def create_dish(self,name,description,price):
        return IndianDish(name,description,price)
    
class ItalianDish(Dish):
    def display(self):
        print("Dish==>name:{},description:{},price:{}$".format(
            self.name,self.description,self.price
        ))
class MexicanDish(Dish):
    def display(self):
        print("Dish==>name:{},description:{},price:{}$".format(
            self.name,self.description,self.price
        ))

restaurant1=ItalianRestaurant()
dish1=restaurant1.create_dish("pizza","flat_food","3000$")
restaurant2=MexicanRestaurant()
mexidish=restaurant2.create_dish("chila","like_mexicanflag,"2500")
dish1.display()
mexidish.display()