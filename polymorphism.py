#polymorphism

#method overriding->(parent(method)into child(method))
#eg:1
class A():
    def display1(self):
        print("A class")
class B(A):
    def display1(self):
        A.display1(self)
        print("B class")
o1=B()
o1.display1()
print("-------------------------------------------------")

#eg:2
class A():
    def display1(self):
        print("A class")
class B(A):
    def display1(self):
        print("B class")
        A.display1(self)
o1=B()
o1.display1()
print("-------------------------------------------------")

#method overloding ->will not support in python


#operator overloading->
#using magic methods od opreators
#magic methods:

#binary opertors
class edex():
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return self.a + other.a
    def __sub__(self,other):
        return self.a - other.a
    def __mul__(self,other):
        return self.a * other.a
    def __floordiv__(self,other):
        return self.a // other.a
    def __truediv__(self,other):
        return self.a / other.a
    def __mod__(self,other):
        return self.a % other.a
    def __pow__(self,other):
        return self.a ** other.a
    def __rshift__(self,other):
        return self.a >> other.a
    def __lshift__(self,other):
        return self.a << other.a
    def __and__(self,other):
        return self.a & other.a
    def __or__(self,other):
        return self.a | other.a
    def __xor__(self,other):
        return self.a ^ other.a
o1=edex(5)
o2=edex(10)
print(o1+o2)
print(o1-o2)
print(o1*o2)
print(o1//o2)
print(o1/o2)
print(o1%o2)
print(o1**o2)
print(o1>>o2)
print(o1<<o2)
print(o1&o2)
print(o1|o2)
print(o1^o2)
print("------------------------------------------------------")

#comparision operators:
class edex():
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        return self.a < other.a
    def __gt__(self,other):
        return self.a > other.a
    def __le__(self,other):
         return self.a <= other.a
    def __ge__(self,other):
        return self.a >= other.a
    def __eq__(self,other):
        return self.a == other.a
    def __ne__(self,other):
        return self.a != other.a
o1=edex(5)
o2=edex(10)
print(o1<o2)
print(o1>o2)
print(o1<=o2)
print(o1>=o2)
print(o1==o2)
print(o1!=o2)
print("------------------------------------------------------")



#assignment operators
class Edex:
    def __init__(self, a):
        self.a = a
    def __iadd__(self, other):
        return  self.a += other.a

o1 = Edex(5)
o2 = Edex(15)
print(o1+=o2)










    
    


