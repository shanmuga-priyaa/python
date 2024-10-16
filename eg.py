#eg:1
'''num=int(input("ebter the number:"))
i=1
fact=1
while i<=num:
    fact=fact*i
    i+=1
print(fact)'''

#eg:2
'''num=123
rev=0
while num>0:
    server=num%10
    rev=rev*10+server
    num=num//10
print(rev)'''






#eg:
'''row=int(input("Enter the row="))
for i in range(1,row+1):
    print(" "*(row-i),end="")
    
    for j in range(2*i-1):
        print("*",end="")
    print()
print("-------------------------------------------------")'''

#geting a value to print tuple,set,dict,list by the user using there limit and print it

#eg:0
'''num=int(input("enter the limit:"))
list1=[]
for i in range(1,num+1):
    n=int(input("enter the integer:"))
    list1.append(n)
print("list:",list1)
tup=tuple(list1)
print("typle:",tup)
S1=set(list1)
print("set:",S1)'''

#eg:1
'''num=int(input("enter the limit:"))
dict={}
for i in range(1,num+1):
    key=int(input("enter the key:"))
    value=input("enter the value:")
    dict.update({key: value})
print(dict)'''

'''def count(string):
    letter_counts = {}
    for char in string:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
    output = {"word": letter_counts}   
    return output

string = "shanmuga priyaa".lower() 
result = count(string)
for char, count in result["word"].items():
    print(f"{char}-{count}")'''


#eg:
'''word=input("enter the word:")
d1={}
for i in word:
    if i==" ":
        i="space"
        d1[i]=1
    if i in d1:
        d1[i]+=1
    else:
        d1[i]=1
print(d1)'''

#task-1
class treasure():
    def box1(self):
        key1=int(input("key1:"))
        print("gold")
    def box2(self):
        key2=int(input("key2:"))
        print("gold")
    def box3(self):
        key3=int(input("key3:"))
        print("gold")+
Dora=treasure()
Dora.box1()
Dora.box2()
Dora.box3()
print("the end")
    






    

        
