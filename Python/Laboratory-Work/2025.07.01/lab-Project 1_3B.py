import random
import names

#Exersize 1
RandomNumbers = [random.randint(1, 100) for i in range(10)]

Mediane = 50
for Number in RandomNumbers:
    if Number < Mediane:
        print(Number, "Lower")
    else:
        print(Number, "Higher")

#Exersize 2
NamesList = [names.get_first_name() for i in range(10)]
GroupAM = []
GroupNZ = []

for name in NamesList:
    FirstLetter = name[0].upper()
    if 'A' <= FirstLetter <= 'M':
        GroupAM.append(name)
    else:
        GroupNZ.append(name)

print("Names from A to M:", GroupAM)
print("Names from  N to Z:", GroupNZ)

#Exersize 3
Poem = ""
while True:
    Word = input("Please enter words for Poem (Empty string = finish): ")
    if Word == "":
        break
    Poem += Word[0]
print("Poem from the first letters of each word:", Poem)

