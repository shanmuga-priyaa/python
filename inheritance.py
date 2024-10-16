#inhetitance

#eg:1
class father():            #parent class
    house="house father"
    def display1(self):
        print(self.house)
class son(father):      #child class
    bike="son bike"
    def display2(self):
        print(self.bike)
o1=son()
print(o1.bike)   #child class properties
o1.display1()
print(o1.house)   #parent class properties
o1.display2()
print("_____________________________________________________")

#inheritance type
#1-->single in heritance
class father():            
    house="house father"
    def display1(self):
        print(self.house)
class son(father):      
    bike="son bike"
    def display2(self):
        print(self.bike)
o1=son()
print(o1.bike)   
print(o1.house)   
o1.display2()
print("_____________________________________________________")

#multilevel
class A():#parent class

    def display1(self):
        print("A class")  
class B(A):          #both parent class and child class->access a,b
    def display2(self):
        print("B class")   
class C(B):          #child class->access a,b,c
    def display3(self):
        print("C class")   
o3=C()
o3.display3()
print("_____________________________________________________")

#multiple
class A():
    def display1(self):
        print("A class")
class B():
    def display2(self):
        print("B class")
class C():
    def display3(self):
        print("C class")
class D(A,B,C):
    def display4(self):
        print("D class")
o1=D()
o1.display1()
o1.display2()
o1.display3()
o1.display4()
print("_____________________________________________________")

#hieraarichal
class A():
    def display1(self):
        print("A class")
class B(A):
    def display2(self):
        print("B class")
class C(A):
    def display3(self):
        print("C class")
class D(A):
    def display4(self):
        print("D class")
o1=A()
o2=B()
o3=C()
o4=D()
o1.display1()
o2.display2()
o3.display3()
o4.display4()
print("_____________________________________________________")

#hybrid(hierarichal,multilevel)
class A():
    def display1(self):
        print("A class")
class B(A):
    def display2(self):
        print("B class")
class C(A):
    def display3(self):
        print("C class")
class D(C):
    def display4(self):
        print("D class")
class E(D):
    def display5(self):
        print("E class")
o1=C()
o1.display3()
o2=D()
o3=E()
o2.display4()
o3.display5()
print("_____________________________________________________")

#eg:2
#--->MRO(error : method resolution order it is not in order)

class A():
    def display1(self):
        print("A class")
class B(A):
    def display2(self):
        print("B class")
class C(B):
    def display3(self):
        print("C class")
class D(C,B,A):
    def display4(self):
        print("D class")
o1=D()
o1.display1()
o1.display2()
o1.display3()
o1.display4()
print("_____________________________________________________")





    



        


    
    
    
