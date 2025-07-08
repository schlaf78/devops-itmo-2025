
#Iterations count
#1,2,3
n = int(input('Задайте число '))
k = 0
Transit = n
while n > 0:
    n = n//10 # Отбрасывание последней цифры числа n
    k = k + 1
print("Количество цифр в числе", k)
#Numbers count
print("Digits summ is:",sum(int(d) for d in str(Transit)))

#Max disributor finding
