'''
Напишите программу, которая будет запрашивать у пользователя значения
продаж магазина за каждый день недели и сохранять их в виде списка. Примените
цикл, чтобы вычислить общий объем продаж за неделю и показать результат. Затем
программа должна вывести на экран все введенные пользователем числа в порядке
возрастания – по одному значению в строке. Используйте для сортировки либо
метод sort, либо функцию sorted.
'''

WeekSales = []

for i in range(7):
    DailyProfit = int(input("Please enter Daily Trade Amount per day: "))
    WeekSales.append(DailyProfit)

GrandTotal = sum(WeekSales)
print(f"Grand Total:", GrandTotal)

print(sorted(WeekSales))

