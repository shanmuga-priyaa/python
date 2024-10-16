#eg:1
'''num=int(input("enter the number:"))
i=1
fact=1
while i<=num:
    fact=fact*i
    i+=1
print(fact)
print("--------------------------------------------------")

#eg:2
num=123
rev=0
while num>0:
    server=num%10
    rev=rev*10+server
    num=num//10
print(rev)
print("-------------------------------------------------")

#eg:3
num=int(input("Enter an number: "))
num1=num
rev=0
while num>0:
    server=num%10
    rev=rev*10+server
    num=num//10
if num1==rev:
    print("The number is Palindrome")
else:
    print("The number is not a Palindrome")
print("--------------------------------------------------")

#eg:4
num=int(input("Enter a number: "))
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
print(sum)
print("-------------------------------------------------")

#eg:5
num=int(input("Enter the values: "))
if (num%2==0 and num%3==0):
    print("The num is divisible by both 2 and 3)
elif num%2==0:
     print("The num is divisible by 2 but not divisible by 3)
elif num%3==0:
     print("The num is not divisible by 2 but divisible by 3)
else:
    print("The num is not divisible by both 2 and 3")
print("---------------------------------------------------------")

#eg:6
num1="spark"
num2=AEIOUaeiou
Vowels=0,Consonants=0
for i in num1
if i in num2
vowels+=1
else:
Consontants+=1
print("-------------------------------------------------")

#eg:7
name=input("Enter a string: ")
name1=input("Enter the substring: ")
name2=input("Enter the new substring: ")
name3=(name.replace(name1,name2))
print(name3)

name="Hello World"
print(name)
print(name.replace("Hello World","HelloWorld"))
print("-------------------------------------------------")

#eg:7
num1=input("Enter the word: ")
num2="AEIOUaeiou"
v,c=0,0
for i in num1:
    if i in num2:
        v+=1
    else:
        c+=1
print("vowels=" + str(v))
print("consonants=" + str(c))
print("-------------------------------------------------")

#eg:8
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
print("-------------------------------------------------")


#eg:9
row=int(input("Number of rows="))

-or i in range(1,row+1):
    print(" "*(row-i),end="")
    
    for j in range(1,i+1):
        print("* ",end="")
        
    print()
print("-------------------------------------------------")
 
#eg:10
row=int(input("Enter the row="))
for i in range(1,row+1):
    print("  "*(row-i),end="")
    
    for j in range(2*i-1):
        print("* ",end="")
        
    print()
print("-------------------------------------------------")


#eg:11
row=int(input("Enter the row="))
for i in range(1,row+1):
    print(" "*(row-i),end="")
    
    for j in range(2*i-1):
        print("*",end="")
    print()
print("-------------------------------------------------")'''


#2 *i -1 --->1
#2 * 2-1 --->3
#2 * 3 - 1 -->5

