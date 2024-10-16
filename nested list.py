#nested list->(nlist)
#indexing the nested list
#eg:1
list=([1,2,3],[4,5,6])
print(list[1][1])
print(list[0][1])
print("'''''''''''''''''''''''''''''''''''''''''")
#eg:2
#nlist(slicing)
list=([1,2,3],[4,5,6],[7,8,9,10])
print(list[2][1:4])
print("'''''''''''''''''''''''''''''''''''''''''")

#eg:3
#nlist(indexind)
list=([1,2,3],[4,5,6])
for i in list:
    for j in i:
        print(j)
print("'''''''''''''''''''''''''''''''''''''''''")

























+
#eg:4
num=int(input("enter the limit of the list:"))
list=[]
for i in range(1,num+1):
    n=int(input("enter an integer:"))
    list.append(n)
print(list)
