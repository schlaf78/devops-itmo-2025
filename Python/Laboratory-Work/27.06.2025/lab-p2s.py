#Exersize 3
string1 = "This is string."
string2 = "     This is one more string." #5 spaces for LSTRIP

string_summary = string1 + string2
print ("Result: ",string_summary)

print("String 1 length:", len(string1))
print("String 1 uppering case:", string1.title())
print("String 1 lowering case:", string1.lower())
print("String 1 end space deleting:", string1.rstrip())
print("String 2 beginning space deleting:", string2.lstrip())
print("String 2 both sides space deleting:", string2.strip())
print("String 2 e letter  deleting:", string2.strip('.'))

print("string1" + str(15))
print(15 + int("25"))

#Strings formating part
a = 1/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))