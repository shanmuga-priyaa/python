#eg:1
'''list1=["Edex",1,4,5]
list2=["Tech",3,4,5]
print(list1)
print(list1[0])
print(list1[2:4])
print(list1[1:4])
print(list2+list2)
print(list1+list2)
print("-------------------------------------------------")'''

#eg:2
'''list=[10,20,30,"New Delhi","Mumbai"]
print("List element are:",list)
list.extend([40,50,"chennai"])
print("List elements:",list)
list.pop()
print("List elements:",list)
list.pop()
print("List elements:",list)
print("-------------------------------------------------")'''

#eg:3
'''list=[10,20,30,40,50]
sum=0
print("list elements are:")
for i in list:
    print(i)
    sum+=i
print("sum is:",sum)    
print("-------------------------------------------------")'''

#eg:4
'''list=[10,20,30,40,30]
list.remove(30)
print("List after removing 30:",list)
list.remove(10)
print("List after removing 10:",list)
print("-------------------------------------------------")'''

#eg:5
'''list=[10,20,10,30,10,40,10,50]
print("original list:",list)
num=int(input("original list:"))
for i in list:
    if i == num:
        list.remove(num)
print("list after removing:")
print("-------------------------------------------------")'''
                

#eg:6
'''list=[10,20,30,40,50]
print("original list:",list)
list.pop(1)
list.pop(1)
print("list after removing elements:",list)
print("-------------------------------------------------")'''

#eg:7
'''list=[10,20,10,20,30,40,50]
name=int(input("Enter index value:"))
if i in list:
    index=list.index(name)
    print("print the index of the 1st element",name,"is:",index)
else:
    print("element not found in the list:")
print("-------------------------------------------------")'''

#eg:8
'''num=int(input("Enter the limit:"))
list=[]
for i in range(1,num+1):
    n=int(input("Enter an integer:"))
    list.append(n)
print(list)
print("-------------------------------------------------")'''


#eg:9
'''list1=[10,20,10,20,30,40,30,50]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)
print("-------------------------------------------------")'''


#eg:10
'''list =[11,22,33,44,55]
evenum = []
oddnum= []
for i in list:
    if i % 2 == 0:
        evenum.append(i)
    else:
        if i % 2 != 0:
            oddnum.append(i)
print("List with EVEN numbers:", evenum)
print("List with ODD numbers:", oddnum)
print("-------------------------------------------------")'''
 
#eg:11
'''List = [10, 15, 20, 25, 30]
M = 3
N = 5
for number in List:
    if number % M == 0 and number % N == 0:
        print(number)
print("-------------------------------------------------")'''

#eg:12
'''Start = 1
End = 10
numbers = []
squares = []
cubes = []
for number in range(Start, End + 1):
    numbers.append(number)       
    squares.append(number ** 2) 
    cubes.append(number ** 3)
print("numbers:", numbers)
print("squares:", squares)
print("cubes  :", cubes)
print("-------------------------------------------------")'''


#eg:14
'''list=[10,20,30,40,50,60]
list1=list[:3]
list2=list[3:]
print("list1:",list1)
print("list2:",list2)
print("-------------------------------------------------")'''


#eg:15
'''oddnum = []
for i in list:
    if i % 2 != 0:
        oddnum.append(i)
print("list after removing EVEN numbers")
print("list =", oddnum)
print("-------------------------------------------------")'''

#eg:18
'''num=[4,-1,5,9,-6,2,9,8]
positive=[]
negative=[]
for i in num:
    if i<0:
        negative.append(i)
    else:
        positive.append(i)
print("negative  number:",negative)
print("positive  number:",positive)
print("-------------------------------------------------")'''

#eg:19
'''list=[4,1,6,3,9]
result=1
for i in list:
    result*=i
print(result)
print("-------------------------------------------------")'''

#eg:20
'''list = [3, 6, 9, 8, 1,6]
count = 0
for i in list:
  if i:  
    count += 1
if count:
  print(count)
else:
  print("The list is empty.")
print("-------------------------------------------------")'''

#eg:21
'''list=[4,2,9,5,1,0,7]
i=8
if i in list:
    print("present")
else:
    print("not present")
print("-------------------------------------------------")'''

#eg:22
'''list1=[[2,3,4],[3,2,4],[5,8]]
list2=[]
for i in list1:
    for j in i:
        list2.append(j)
print(list2)
print("-------------------------------------------------")'''















