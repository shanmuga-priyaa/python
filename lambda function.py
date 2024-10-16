#lambda function(map,filter,reduce)

#map
list1=[1,2,3,4,5]
mlist=map(lambda a:a+10,list1)
print(list(mlist))
print("-----------------------------------------------")

#use mostly (arg,exp)
#map error->we print the map in list func so we need as list
'''list1=[1,2,3,4,5]
mlist=map(lambda a:a+10,list1)
print(mlist)
print("-----------------------------------------------")'''

#no dont use condition in map
list1=[1,2,3,4,5]
mlist=map(lambda a:a%2==0,list1)
print(list(mlist))
print("-----------------------------------------------")

#filter
#eg:1
list1=[1,2,3,4,5]
flist=filter(lambda a:a%2==0,list1)
print(list(flist))
print("-----------------------------------------------")

#eg:2
list1=[1,2,3,4,5]
flist=filter(lambda a:a%2!=0,list1)
print(list(flist))
print("-----------------------------------------------")

#filter error->we print the filter in list func so we need as list
'''list1=[1,2,3,4,5]
flist=filter(lambda a:a%2==0,list1)
print(flist)
print("-----------------------------------------------")'''

#reduce->there is no need for changing in list
from functools import reduce
list1=[1,2,3,4,5]
rlist= reduce(lambda a,b:a+b,list1)
print(rlist)
print("-----------------------------------------------")

#map,filter,reduce
from functools import reduce
list1=[1,2,3,4,5,6,7,8,9,10]
mlist=map(lambda a:a**2,list1)
flist=filter(lambda a:a>=3,list1)
rlist=reduce(lambda a,b:a+b,list1)
print(list(mlist))
print(list(flist))
print(rlist)
















