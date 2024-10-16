#decorator
def box(func):                         #decorator fun (func)
    def paper():                       #wrapper fun (paper,box)
        print("cover")                 #original fun(chicken,icecream,dress)
        func()
        print("covered")
    return paper

@box
def chicken():
    print("chicken fried rice")
    print()
def icecream():
    print("arun icecream")
    print()
@box
def dress():
    print("dress")
    
chicken()
icecream()
dress()
print("_________________________________________________________")


#property decorator
class edex():
    @property
    def display1(self):
        print("display1")
    @staticmethod
    def display2():
        print("display2")
o1=edex()
o1.display1
o1.display2()

        


