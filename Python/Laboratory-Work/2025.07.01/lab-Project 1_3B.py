import random
from queue import PriorityQueue

#Exersice 1
RandomNumbers = [random.randint(1, 100) for i in range(10)]
print("Generated array is:",sorted(RandomNumbers))

Mediane = 50
for Number in RandomNumbers:
    if Number < Mediane:
        print(Number, "Lower")
    else:
        print(Number, "Higher")

#Exersize 2
