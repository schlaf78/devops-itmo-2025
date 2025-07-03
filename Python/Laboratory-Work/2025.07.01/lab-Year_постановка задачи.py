import datetime
#Как проверить високосный ли год?
'''
Стандартный год состоит из 365 дней, а високосный из 366 дней.

Правила определения:
Високосный год кратен 4, но при этом не кратен 100, либо кратен 400.
Иными словами, если год делится на 4 без остатка, но делится на 100 только с остатком,
то он високосный, иначе — невисокосный, кроме случая, если он делится без остатка на 400 — тогда он всё равно високосный.
'''
current_date = datetime.date.today()
year = current_date.year               # проверяемая переменная
'''Задание 1. Проверка с условиями if-else
'''

if year % 4 == 0:
    print("1. Year is leap")

else:
   print("1. Year is not leap")

'''Задание 2. Проверка с дополнительными условиями elif
'''
if year % 4 == 0:
    print("2. Year is leap")
elif year % 100 == 0:
    print("2. Year is not leap")
    if year % 400 == 0:
        print("2. Year is leap")
    else:
        print("2. Year is not leap")



'''Задание 3. Проверка с помощью логических операторов в одну строку if
'''
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("3. Year is leap")
else:
    print("3. Year is not leap")


'''Задание 4. Проверка с применением специальной функции модуля calendar
Найдите ее самостоятельно....
'''
import calendar
if calendar.isleap(year):
    print ("4. Year is leap")
else:
    print("4. Year is not leap")
