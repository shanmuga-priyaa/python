#object->instance(we can create,del,acc,but no update)
#eg:1-access
class edex():       
    name="shanmu"
    loc="madurai"
tech=edex()         
print(tech.name)    #acces
print(tech.loc)
print("-------------------------------------------")

#eg:2-create
class edex():       
    name="vijay"
    loc="madurai"
tech=edex()
tech.name="priyaa"     #create
print(tech.name)
print("-------------------------------------------")

#eg:3-del
class edex():       
    name="priyaa"
    loc="madurai"
tech=edex()
tech.name="shanmu"
print(tech.name)
del tech.name
print(tech.name)       #del
'''del tech.name
print(tech.name)'''
print("-------------------------------------------")
