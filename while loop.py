#WHILE LOOP
#ini , condition , inc/dec
'''n=1
while n<=5:
    print(n)
    n+=1'''

#DECREMENT
'''n=5
while n<=1:
    print(n)
    n-=1'''

#SUM OF N NUMBERS
'''num = int(input("enter a value:"))
i=1
sum=0
while i<=num:
    sum=sum+i
    i+=1
print(sum)'''


#FACTORIAL OF N NUMBER
'''num = int(input("Enter a value: "))
i = 1
fact = 1
while i <= num:
    fact=fact*i
    i += 1
print(fact)'''


#whilelooping

#while = condition + looping

    #1 Ascending

'''n = 1
while n<=5:
    print(n)
    n+=1'''
    
     #2 Descending
'''n = 5
while n>=1:
    print(n)
    n-=1'''



    #3(sum of N num)

'''
num = int(input("Enter a value:"))

i=1
sum=0

while i<=num:
    sum=sum+i
    i+=1
    
print(sum)'''

#4(digit of N number)
num=int(input("Enter a number: "))
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
print(sum)


#5(factorial of N num)->multiple


num = int(input("Enter a value:"))

i=1
fact=1

while i<=num:
    fact=fact*i
    i+=1
    
print(fact)


   #6(even and odd):


'''#  while loop to find even numbers
num = int(input("Enter a value: "))
i = 1
while i <= num:
    if i % 2 == 0:
        print("Even numbers are", i)
    i += 1
#  while loop to find odd numbers
i = 1
while i <= num:
    if i % 2 != 0:
        print("Odd numbers are", i)
        i+=1'''

'''num = int(input("Enter a value: "))

# Finding even numbers
print("Even numbers up to", num, "are:")
i = 1
while i <= num:
    if i % 2 == 0:
        print(i, end=" ")  # Print the even number
    i += 1

# Finding odd numbers
print("\nOdd numbers up to", num, "are:")
i = 1
while i <= num:
    if i % 2 != 0:
        print(i, end=" ")  # Print the odd number
    i += 1'''






