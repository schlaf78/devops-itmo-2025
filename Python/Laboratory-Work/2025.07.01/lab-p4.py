
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
a = int(input('Задайте первое число '))
b = int(input('Задайте второе число '))
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
nod = a
print('НОД равен', nod)

#Resource usage
from random import randint # подключение функции из модуля random
total = 100 # запас ресурса
i = 0 # счетчик итераций цикла
while i < 5:
    n = randint(1, 50) # имитация расхода ресурса
    total = total - n
    if total < 0:
        total = 0
        break
    #total = total - n
    i = i + 1
else:
    print("Процесс выполнен полностью")
print("Осталось", total)


#4 Numbers Summ
num = input('Введите число для подсчета суммы цифр: ')
sumIt = 0
for it in num:
    sumIt += int(it)
print(f"Сумма цифр числа {num} равна {sumIt}")

#Test lab of the module
from random import randint
Total = 100

for i in range(5):
    N = randint(1, 50)
    Total -= N
    print(f"Stage {i+1}: Consumed {N}, Resource Left: {max(Total, 0)}")

    if Total <= 0:
        print("Out of resource")
        break
else:
    print("Процесс выполнен полностью")
print("Осталось", max(total, 0))