name = input("Enter user Name: ")
surname = input("Enter user Surname: ")

Name_UpperingCase = name.title()
Surname_UpperingCase = surname.title()
login = (Name_UpperingCase[:1] + Surname_UpperingCase[:4]).title()

print("User name & Surname are:\n",Name_UpperingCase,Surname_UpperingCase,"\nLogin is:",login)