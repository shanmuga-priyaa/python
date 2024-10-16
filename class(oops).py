#class->instance

#attributes-->class instance
#1-> getattribute(acces the attribute)
#eg:1
class edex():
    name="shanmu"
    location="madurai"
print(getattr(edex,"name"))
print(getattr(edex,"location"))
print("-----------------------------------------------------------------------")

#2-> setattributes(create,update)
#eg:1
#create
class edex():
    name="shanmu"
    location="madurai"
setattr(edex,"course","python")
print(getattr(edex,"course"))
print("-----------------------------------------------------------------------")

#eg:2
#update
class edex():
    name="shanmu"
    location="madurai"
setattr(edex,"course","python")
print(getattr(edex,"course"))
setattr(edex,"location","chennai")
print(getattr(edex,"location"))
print("-----------------------------------------------------------------------")

'''#3-> delete attribute
class edex():
    name="shanmu"
    location="madurai"
print(getattr(edex,"name"))
print(getattr(edex,"location"))
delattr(edex,"location")
print(getattr(edex,"location"))
print("-----------------------------------------------------------------------")'''

#------------------->dot notation
#eg:1
#.notation->(access)
class edex():
    name="shanmu"
    location="madurai"
print(edex.name)
print(edex.location)
print("-----------------------------------------------------------------------")

#.notation->(create)
#eg:2
class edex():
    name="shanmu"
    location="madurai"
print(edex.name)
print(edex.location)
edex.course="python"
print(edex.course)
print("-----------------------------------------------------------------------")

#notation-(update)
#eg:3
class edex():
    name="shanmu"
    location="madurai"
edex.location="chennai"
print(edex.location)
print("-----------------------------------------------------------------------")

#.notation->(delete)
#eg:4
'''class edex():
    name="shanmu"
    location="madurai"
    course="python"
del edex.course
print(edex.course)
print("-----------------------------------------------------------------------")'''

