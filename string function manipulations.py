#.method

#string inbuild functions total=20(
#upper()=>upper case print
#lower()=>lower case print
#swap()=>swap the text(lower into upper ,upper into lower)
#type()=>to fuind the data type (string ,or int)
#capitalized()=>set the 1st index word as capital word
#title()=>it will change the every string 1st letter as capital word
#count=>


#string function
#type
'''name="Hii Shanmu"
print(type(name))

#upper
name="Hii Shanmu"
print(name.upper())

#lower
name="Hii Shanmu"
print(name.lower())


#capitalized
name="hii shanmu"
print(name.capitalized())

#title
name="hii shanmu"
print(name.title())

#c0unt
name="hii shanmu"
print(name.count())'''



#indexing->taking one variable
#sclicing->taking multiple variables
#replace->(old,new)
#find,index->we can get the index value

#task-1
'''name="edex tech"
print(name.find("e"))
print(name.find("e",2))
print(name.replace("e","p"))
print(name.index("e",2))'''

#strip->starting and ending space will be removed`
#lstrip->left space will be removed
#rstrip->right space will be remove
#len->length of the variable

'''name="  shanmu hii  "
print(name)
print(name.strip())
print(len(name))

name2=name.strip()
print(name2)
print(len(name2))
print(name.lstrip())
print(name.rstrip())'''




#it will return boolean value
#isupper()
#islower()
#isdigit->digit and numeric are same function but digit is slow compared to numeric
#isnumeric->it is adavnce
#isalpha
#isalnum->both alphabet and numbers are consided

#task-1
'''name="Shanmu123"
print(name.isupper())
print(name.isdigit())
print(name.isnumeric())
print(name.isalpha())
print(name.isalnum())
print(name.islower())'''

#string indexing
name="Edextech"
print(name[6])
print(name[3])
print(name[12])#over than limit
print(name[1:5])
print(name[:5])
print(name[0:6:2])
print(name[:])


#string slicing
name="Edextech"
print(name[-1:-9:-1]
print(name[::-1])#reversing the string    
 
