#constructor->it is a special method
#eg:0
class edex():
    def __init__(self):
        print("i am condstructor")
o1=edex()
print("______________________________________________________________")

#eg:1->the 4th on wull be printed becz i will over lap remaning
class edex():
    def __init__(self):
        print("i am condstructor")
    def __init__(self):
        print("2nd condstructor")
    def __init__(self):
        print("3rd condstructor")
    def __init__(self):
        print("4th condstructor")
o1=edex()
print("______________________________________________________________")

#eg:2
class edex():
    def __init__(self):
        print("i am constructor")
o1=edex()
o2=edex()
o3=edex()
print("__________________________________________________________________")

#eg:3
class mobiles():
    def __init__(self,bname,mname,price):
        self.Brand_name= bname
        self.Model_name= mname
        self.price= price
    def display(self):
        print("Brand name:",self.Brand_name)
        print("Model name:",self.Model_name)
        print("price name:",self.price)
redmi=mobiles("realme narzo 20","note 10pro",100000)
redmi.display()
vivo=mobiles("vivo","v15 pro",80000)
vivo.display()
print("__________________________________________________________________")


#eg:4
class mobiles():
    def __init__(self,bname,mname,ram,price):
        self.Brand_name= bname
        self.Model_name= mname
        self.Ram_name=ram
        self.price= price
    def display(self):
        print("Brand name:",self.Brand_name)
        print("Model name:",self.Model_name)
        print("Ram name:",self.Ram_name)
        print("price name:",self.price)
redmi=mobiles("realme narzo 20","note 10pro","",100000)
redmi.display()
vivo=mobiles("vivo","v15 pro","4GB",80000)
vivo.display()
Iphone=mobiles("Iphone","15 pro","6GB",80000)
Iphone.display()
oppo=mobiles("vivo","v15 pro","",80000)
oppo.display()
samsung=mobiles("vivo","v15 pro","",80000)
samsung.display()
print("__________________________________________________________________")


#eg:5











        

        
    
