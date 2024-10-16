'''age=int(input("enter the age:"))
if age>=18:
    print("candidate is eligible for age:")
    scalary=int(input("enter the scalary:"))
    if scalary>=1000:
        print("candidate is eligible for scalary:")
        loan=int(input("enter the loan amount:"))
        if scalary>=5000:
            print("candidate is eligible for loan amount:")
        else:
            print("candidate is not eligible:loan amount")
    else:
        print("candidate is not eligible:scalary")
             
else:
    print("candidate is not eligible:age")'''




'''username=(input("enter the username:"))
if username=="admin":
             print("valid username")
             password=(input("enter the password:"))
             if password=="password123":
                 print("valid password")
             else:
                     print("succesfully logined")
else:
    print("invalid username")'''



age=int(input("enter the age:"))
if age>=18 and age<=100:
    gener=input("[comedy / thriller]:").lower()
    if gener == "comedy":
        print("kalakalapu")
    elif gener == "thriller":
        print("leo")
    else:
        print("invalid")
        
elif age<18 and age>0:
    gener=input("[comedy / thriller]:").lower()
    if gener == "comedy":
        print("shinchan")
    elif gener == "thriller": 
        print("tom and jerry")
    else:
        print("invalid")
    
         
