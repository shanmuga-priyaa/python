#tuple()

#eg:1
'''#indexing,slicing
tuple=(1,2,3,4,5,2,3)
tup=("apple","orange")
print(tuple)
print(tuple[2])
#allow dublicate valube
print(tuple[2:])
#but we can use new variable la stroe pana + wrk agum
c_tup=tuple+tup
print(c_tup)
#we cant change,add,remove->(mutable)
tuple[2]="apple"
tuple.extend(444)
tuple=tuple+tuple1
print(tuple)

#eg:2
#unpacking(seperate and assige the values)
tup=(1,2,3)
a,b,c=tup
print(a)
print(b)
print(c)
print("-------------------------------------")


#eg:3
#unpacking with *  
tup=(1,2,6,8,3,9,5,6)
a,b,c,d,*e=tup
print(a)
print(b)
print(c)
print(d)
print(e)
print("--------------------------------------------")

#eg:4
#typle->(finding the data type)
a=(1)
b=("hello")
c=(1.234)
d=("apple","orange","mango")
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print("--------------------------------------------")

#eg:5
#packing->it is used without () it will convert into tuple
tuple=1,2,3,"apple"
print(tuple)
print("--------------------------------------------")

#eg:6
#tuple with type casting
tup=(1,2,3,4,5)
change=list(tup)
change.remove(3)
change.append("apple")
new=tuple(change)
print(new)
print("--------------------------------------------")'''


#eg:7

list1=[10,20,10,20,30,40,30,50]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)






