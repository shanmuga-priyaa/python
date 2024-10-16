#sum of n numbers using recursion function
#recursion
#eg:1
def sumn(n):
    if n==1:
        return 1
    else:
        return n+sumn(n-1)
print(sumn(5))
print("------------------------------------------------")
#eg:2
def sumn(n):
    #if n==1:
        #return 1
    if n==0:
        return 0
    else:
        return n+sumn(n-1)
print(sumn(0))
print("------------------------------------------------")
#eg:3
def sumn(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return n+sumn(n-1)
print(sumn(0))
print("------------------------------------------------")


#factorial
#eg:1
def sumn(n):
    if n==1:
        return 1
    else:
        return n*sumn(n-1)
print(sumn(5))
print("------------------------------------------------")
#eg:2
def sumn(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return n*sumn(n-1)
print(sumn(5))
print("------------------------------------------------")

#sum od digits using recursion
#
