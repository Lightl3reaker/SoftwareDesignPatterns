from abc import ABC,abstractclassmethod

#Factory interface
class Factory(ABC):
    #abstract method
    @abstractclassmethod
    def product(self):
        pass

#Concrete Factories
class Factory1(Factory):
    def product(self):
        return f'Product from {self.__class__.__name__}'
class Factory2(Factory):
    def product(self):
        return f'Product from {self.__class__.__name__}'

#Creator Interface
class FactoryCreator(ABC):
    @abstractclassmethod
    def factorycall(self):
        pass
    
    def showproduct(self):
        factory=self.factorycall()
        result=factory.product()
        return result

#Concrete Creators For Factory
class Creator1(FactoryCreator):
    def factorycall(self):
        return Factory1()

class Creator2(FactoryCreator):
    def factorycall(self):
        return Factory2()

#Client Codes
user1=Creator1()
print(user1.showproduct())
user2=Creator2()
print(user2.showproduct())
