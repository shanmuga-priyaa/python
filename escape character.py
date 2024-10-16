#Escape characters


'''print("hello\nworld")  # \n -> new line
print("shilpa\tsherin") # \t -> text space
print("hello\bwelcome") # \b -> back space dlt
print("father\'s son")  # single quote
print("father\"s son") #double quote
print("10\\5")  #backslash'''



   #Task-1
'''print("Resume:-\n")
print("Full Name\t: SHILPA SHERIN.S\n")
print("Mobile No\t: 6385476310\n")
print("Address\t\t: Manamadurai\n")
print("Email\t\t: shilpasherin06@gmail.com\n")
print("Degree\t\t: Msc.Computer Science\n")'''



# Collecting user inputs

fullName = input("Enter your full name: ").upper()
mobileNo = input("Enter your mobile number: ")
emailId = input("Enter your email id: ")
address = input("Enter your address: ")

degree1 = input("Enter your first degree and stream : ")
yearOfPassing1 = input("Enter year of passing for " + degree1 + ": ")
percentage1 = input("Enter percentage for " + degree1 + ": ")

degree2 = "HSC"
yearOfPassing2 = input("Enter year of passing for " + degree2 + ": ")
percentage2 = input("Enter percentage for " + degree2 + ": ")

degree3 = "SSLC"
yearOfPassing3 = input("Enter year of passing for " + degree3 + ": ")
percentage3 = input("Enter percentage for " + degree3 + ": ")

#escape sequences
resume = fullName + "\n"
resume += "-" * 70 + "\n"
resume += "Mobile no.: " + mobileNo + "\t\tEmail id: " + emailId + "\n"
resume += "Address   : " + address + "\n"
resume += "-" * 70 + "\n"
resume += "Education:\n"
resume += "Degree & Stream\t\tYear of Passing\t\tPercentage\n"
resume += degree1 + "\t\t\t\t" + yearOfPassing1 + "\t\t" + percentage1 + "\n"
resume += degree2 + "\t\t\t\t" + yearOfPassing2 + "\t\t" + percentage2 + "\n"
resume += degree3 + "\t\t\t\t" + yearOfPassing3 + "\t\t" + percentage3 + "\n"
resume += "-" * 70 + "\n"
print(resume)
