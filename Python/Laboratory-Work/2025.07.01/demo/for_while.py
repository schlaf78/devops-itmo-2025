# применение циклов для подсчета суммы элементов последовательности
lst = [11, 23, 15, 17, 19]
sum1 = 0
for i in lst:
   sum1 += i

print(sum1)


sum2 = 0
while lst:
    sum2 += lst[0]
    lst = lst[1:]

print(sum2)



