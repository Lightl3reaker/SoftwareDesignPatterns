from abc import ABC,abstractclassmethod

#PEPSI FACTORY INTERFACE   
class PEPSI(ABC):
    @abstractclassmethod
    def product(self):
        pass

#departments from pepsi that produces respective product under PEPESI
class pepsi(PEPSI):
    def product(self):
        #this need to use print()
        return f"Here is your {self.__class__.__name__}"
class sting(PEPSI):
    def product(self):
        #this doesn't need just call method
        print("Here is your {}".format(self.__class__.__name__))
class miranda(PEPSI):
    def product(self):
        print("Here is your {}".format(self.__class__.__name__))
  
#SUPPLIER CREATOR INTERFACE
class Supplier(ABC):
    #with this method suppliers accesss to get goods from PEPSI Factory
    @abstractclassmethod
    def factoryaccess(self):
        pass
    def showproduct(self):
        goods=self.factoryaccess()
        result=goods.product()
        return result
      
#suppliers that supplies their respective goods to customers
class PepsiSupplier(Supplier):
    def factoryaccess(self):
        return pepsi()
class StingSupplier(Supplier):
    def factoryaccess(self):
        return sting()


#client code
#creating suppliers for desire product and order them
supplier1=PepsiSupplier()
supplier2=StingSupplier()
print(supplier1.showproduct())
supplier2.showproduct()