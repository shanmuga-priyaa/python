#abstract method->it is like a blue print(which has the methods to use)
print("________abstract method_____________")

from abc import ABC,abstractmethod   #-->ABC(default method)
class product(ABC):
    @abstractmethod
    def product_type(self):
        pass                  #-->in abstract we can pass the value directly without using print
    @abstractmethod
    def price(self):
        pass
#__________________________________________________________
class Mobile(product):
    def product_type(self):
        print("product Type:Mobile")
    def brand_name(self):
        print("brand name:redmi")
    def price(self):
        print("price:",2000)
o1=Mobile()
o1.product_type()
o1.brand_name()
o1.price()
print("__________________________________________________")
