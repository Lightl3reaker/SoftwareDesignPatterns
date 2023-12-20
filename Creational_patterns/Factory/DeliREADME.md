
# OnlineDelivery
## Problem
You are building a software system for an online food delivery service. The system should be able to handle different types of restaurants, each offering a unique menu of dishes.<br>
## Requirements:
### Restaurant Types:

There are three types of restaurants: Italian, Mexican, and Indian.
Each restaurant type has its own menu of dishes.<br>
### Dishes:

Each restaurant can offer multiple dishes.
Dishes have attributes like name, description, and price.
<br>

### Ordering:

Users should be able to place orders for dishes from different restaurants.<br>
### Factory Pattern:

Use the Factory Method design pattern to allow the creation of restaurant objects without specifying their concrete classes.

## Your Task:
### Define Interfaces:

Create interfaces for Restaurant and Dish.

### Concrete Classes:

Implement concrete classes for ItalianRestaurant, MexicanRestaurant, and IndianRestaurant that implement the Restaurant interface.
Implement concrete classes for ItalianDish, MexicanDish, and IndianDish that implement the Dish interface.

## Factory Methods:

Implement factory methods in the Restaurant interface for creating instances of Dish.
Each concrete restaurant class should provide its own implementation of these factory methods to create dishes specific to that restaurant.

## Client Code:

Write client code that creates instances of restaurants and orders dishes without knowing their concrete classes.
Testing:

Demonstrate that the system allows users to place orders from different types of restaurants without tightly coupling the client code to specific restaurant implementations.

# Define interfaces
class Restaurant:
    def create_dish(self, name, description, price):
        pass

class Dish:
    def display(self):
        pass

# Implement concrete classes
class ItalianRestaurant(Restaurant):
    def create_dish(self, name, description, price):
        return ItalianDish(name, description, price)

class MexicanRestaurant(Restaurant):
    def create_dish(self, name, description, price):
        return MexicanDish(name, description, price)

class IndianRestaurant(Restaurant):
    def create_dish(self, name, description, price):
        return IndianDish(name, description, price)

class ItalianDish(Dish):
    def display(self):
        print("Italian Dish: ", self.name, self.description, self.price)

class MexicanDish(Dish):
    def display(self):
        print("Mexican Dish: ", self.name, self.description, self.price)

class IndianDish(Dish):
    def display(self):
        print("Indian Dish: ", self.name, self.description, self.price)

# Client code
italian_restaurant = ItalianRestaurant()
mexican_restaurant = MexicanRestaurant()
indian_restaurant = IndianRestaurant()

dish1 = italian_restaurant.create_dish("Pizza Margherita", "Classic Italian pizza", 12.99)
dish2 = mexican_restaurant.create_dish("Tacos al Pastor", "Marinated pork tacos", 9.99)
dish3 = indian_restaurant.create_dish("Chicken Tikka Masala", "Grilled chicken in a creamy sauce", 14.99)

# Display dishes
dish1.display()
dish2.display()
dish3.display()
This problem will help you practice implementing the Factory Method design pattern in a real-world context.






