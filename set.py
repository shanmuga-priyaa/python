'''#set

#does not allow the dublicate

s1={1,5,7,10,20}
#add----->add(),update()
s1.add("apple")
print(s1)
print("-------------------------------------------")

#updating the set
s1={1,5,7,10,20}
s1.update({"apple","orange","mango"})
print(s1)
print("-------------------------------------------")

#updating a string
s1={1,5,7,10,20}
s1.update("apple")
print(s1)
print("-------------------------------------------")

#updating while removing duplicate
s1={1,5,7,10,20}
s2={1,5,12,11}
s2.update(s1)
print(s1)
print("-------------------------------------------")

#set->pop()->it will not no which index to pop so we will not use pop
s1={1,20,33,250,"apple","mango",4.677,5,444}
s1.pop()
print(s1)
print("-------------------------------------------")'''

'''#set-remove()->if we remove the same value it will show error (not a key)
s1={10,22,33,14,"apple","mango"}
s1.remove("apple")
print(s1)
s1.remove("apple")
print(s1)
print("-------------------------------------------")'''

'''#set-discard()->if we remove the same value it will not shiw error,but it will ring the out put
s1={10,22,33,14,"apple","mango"}
s1.discard("apple")
print(s1)
s1.discard("apple")
print(s1)
print("-------------------------------------------")'''

#set-del()->it will delete complete set ,i will show error as(name is not defin)
s1={10,22,33,14,"apple","mango"}
del s1
print(s1)
print("-------------------------------------------")

#set-clear()->it will clear the set values
s1={10,22,33,14,"apple","mango"}
s1.clear()
print("-------------------------------------------")
print(s1)

