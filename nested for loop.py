#simple range concept
'''for i in range(1,4):
    print("shanmu")
    for j in range(1,4):
        print("priyaa")'''



#nestedforloop

'''for i in range(1,4):
    print("Hello")
    for j in range(1,4):
        print("world")'''


        #task-1(week4-day7)

        
'''for i in range(1,5):
    print("week",i)
    for j in range(1,8):
        print("\tDay",j)'''



        #task-2(condition)

'''for i in range(1,5):
    print("week",i)

    if i == 4:
        for j in range(1,4):
            print("\tDay",j)
    else:
        for k in range(1,8):
            print("\tDay",k)'''



      #task-3 (reversing a integer)sum of N num:

'''num=123
rev=0

while num > 0:
    server=num%10
    rev=rev*10+server
    num=num//10

print(rev)'''



       #task-4(sum of digit number):



'''num=int(input("Enter a value : "))

sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit  

    num = num // 10

print(sum)'''




      #task-5(sum of even number):


'''num = int (input("Enter a value : "))

sum = 0

for i in range(1,num+1):
    if i%2 == 0:
        sum = sum + i

print(sum)'''





'''num = int (input("Enter a value : "))

sum = 0

for i in range(1,num+1):
    if i%2 == 0:
        print(i,end="+")
        sum = sum + i

print("\b=",sum)'''




#days and week
'''for i in range(1,2):
    print("week1")
    for j in range(1,2):
        print("day1")
        print("day2")
        print("day3")
        print("day4")
        print("day5")
        print("day6")
        print("day7")
for i in range(1,2):
    print("week2")
    for j in range(1,2):
        print("day1")
        print("day2")
        print("day3")
        print("day4")
        print("day5")
        print("day6")
        print("day7")
for i in range(1,2):
    print("week3")
    for j in range(1,2):
        print("day1")
        print("day2")
        print("day3")
        print("day4")
        print("day5")
        print("day6")
        print("day7")
for i in range(1,2):
    print("week4")
    for j in range(1,2):
        print("day1")
        print("day2")
        print("day3")
        print("day4")
        print("day5")
        print("day6")
        print("day7")'''

#days and week
'''for i in range(1,5):
    print("week",i)
    for j in range(1,8):
        print("\tDays",j)
    print() '''   

#days and week
'''for i in range(1,4):
    print("week",i)
    for j in range(1,8):
        print("\tday",j)
for k in range(1,2):
    print("week",4)
    for l in range(1,4):
        print("\tdays",l)'''

#days and week
'''for i in range(1,5):
    print("week",i)
    if i==4:
        for j in range(1,4):
            print("\t days",j)
    else:
        for k in range(1,8):
            print("\t days",k)'''


#patten program

#ex 1
'''for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()'''
    


#ex 2
'''for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()'''
'''row=int(input("row="))
for i in range(1,row+1):
    print(" "*(row-i),end="")
    
    for j in range(1,i+1):
        print("* ",end="")
        
    print()'''



#ex 3
'''row=int(input("row="))
for i in range(row,0,-1):
    print(" "*(row-i),end="")
    
    for j in range(1,i+1):
        print("* ",end="")
        
    print()'''


#ex 4
'''row=int(input("row="))
for i in range(1,row+1):
    print(" "*(row-i),end="")
    
    for j in range(1,i+1):
        print("* ",end="")
    print()
for i in range(row,0,-1):
    print(" "*(row-i),end="")
    
    for j in range(1,i+1):
        print("* ",end="")
        
    print()'''


        


        


        
        

