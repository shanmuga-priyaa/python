#encapsulation->buind both (attributes/methods)

#access modifiers:
#---->private(__name="edex")
#---->protected(_name="edex")
#---->public(name="edex")

#eg:
#structure
'''class edex():
    def  display(self):
        self.name="edex"        #-->inside class
        self_loc="madu"
        self__year=2024
#-------------------------------------------------
class tech(edex):
    def display2(self):
        print("name:",self.name)
        print("loc:",self._loc)        #--->sub class
        print("year:",self.__year)
#------------------------------------------------
o1=tech()
print("name:",o1.name)
print("loc:",o1._loc)        #--->outside class
print("year:",o1.__year)
print("----------------------------------------------------------")'''


#eg:1
class edex():
    name="edex"        #public
    _loc="madurai"    #protected
    __year=2024       #private
    def display(self):
        print()
        print("Inside class")
        print(self.name)
        print(self._loc)
        print(self.__year)
#---------------------------sub class---------------------
class tech(edex):
    def display2(self):
        print()
        print("sub class")
        print(self.name)        #public
        print(self._loc)        #protected
#---------------------------outside class----------------
o1=tech()
print()
print("outside class")
print(o1.name)               #public
print(o1._loc)              #protected
o1.display()
o1.display2()


#METHOODS
#ACESS MODIFIER
#if a method is private we need to store in another method
class edex():
    __year = 2024
    def method1(self):
        print("public method")
        
    def __method2(self):
        print("private method")
        
    def method3(self):
        print(self.__year)
        
    def method4(self):
        return self.__method2()
    
class tech(edex):
    def display(self):
        print("hii")

o1=edex()
o1.method3()
o1.method4()




























    
