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


#arguments types->tuple result
#(1)arbitary arguments
def default(*data):
    print(data)
default("shanmu")
default("priyaaa",22)
default("hi","bi","good")
print("--------------------------------------------------------------")

    
#(2)key words arguments
def default(name,loc):
    print("name:",name)
    print("location:",loc)
default("shanmu","madurai")
print("--------------------------------------------------------------")

#(3)arbitary keywords arguments->result in dictionary
def default(**data):
    print(data)
default(name="priyaa",age=21,location="madurai")
print("--------------------------------------------------------------")

#(4)Default Arguments
def stu(name,loc="coimbatore",course="python"):
    print(name,loc,course)
stu("Vijay","madurai","java")
stu("Ajith")



'''def stu(a=0,b,c):  1
    print(a,b,c)

stu(5,6)'''
print("_____________")
#(5)passing a list:
def display(a):
    print(a)
display(5)
display([1,2,3,4,5])
print("---------------------------")




