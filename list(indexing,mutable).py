name=["apple","orange","mango",1,2,3]
print(name[1])
print(name[0:2])
print(name[1:5])
print(name[::-1])#reverse we use

#mutable C-A-R
list=["apple","orange","mango"]
#change
list[2]="grapes"
print(list)

#add---->append(),insert(),extend(),+
#append()
list=["apple","orange","mango"]
list.append("edex tech")
print(list)

#insert()
list=["apple","orange","mango"]
list.insert(1,"edex tech")
list.insert(5,"edex tech")
print(list)

#extend()
#eg:1
list=["apple","orange","mango"]
list1=[1,2,3,4]
list.extend(list1)
print(list)

#eg:2
list=["apple","orange","mango"]
list.extend([1,2,3,4,5])
print(list)

#+
list1=["apple","orange","mango"]
list2=[1,2,3,4,5]
list1=list1+list2
print(list1)

#remove
#in remove we can remove what we want but we cant give the index value
list1=["apple","orange","mango"]
print(list1)
list1.remove("apple")
print(list1)
list1.remove("mango")
print(list1)

#pop()
#it will remove from last
#and also we can give the index valuse to remove
#eg:1
list1=["apple","orange","bnana"]
list1.pop()
list1.pop()
list1.pop()
print(list1)

#eg:2
list1=["apple","orange","bnana"]
list1.pop(2)
print(list1)


#clear()
#used to clear the value in list
list1=["apple","orange","bnana"]
list1.clear()
print(list1)

#delete
#used to delete the entire list
#it will show the name error not sefined
list1=["apple","orange","bnana"]
del list1
print(list1)'''

#copy
#= ->it is mean by deap copy
#.coppy ->copy as it is 
shanmu=["apple","orange","mangp"]
shanmu1=shanmu
shanmu2=shanmu.copy()
shanmu.remove("orange")
print(shanmu1)
print(shanmu2)




