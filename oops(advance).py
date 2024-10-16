#oops

#for function key words
#def->define the func name
#eg:1->it will not show out put becz we have never called the function
def display():
    print("shanmu")
print("--------------------------------------------------------------")

#eg:2
def display():
    print("shanmu")
display()
print("--------------------------------------------------------------")

#return and argumentkeywords:
def display():
    return "shanmu"
print(display())
print("--------------------------------------------------------------")

#passing without the arguments
def default():
    a=10
    b=20
    print(a+b)
default()
print("--------------------------------------------------------------")

#passing with arguments
def default(a,b):
    print(a+b)
default(10,20)
print("--------------------------------------------------------------")

'''#argument with error
#here we have nort given the values for a,b
def default(a,b):
    print(a*b)
default()
print("--------------------------------------------------------------")'''


#return+arguments types
#no return with arguments
def default(a,b):
    print(a*b)
default(10,20)
print("--------------------------------------------------------------")

#no return without the arguments
def default():
    a=10
    b=10
    print(a+b)
default()
print("--------------------------------------------------------------")

#return with arguments
def default(a,b):
    return a+b
print(default(10,30))
print("--------------------------------------------------------------")

#return without arguments
def default():
    a=10
    b=7
    return a*b
print(default())
print("--------------------------------------------------------------")


    




