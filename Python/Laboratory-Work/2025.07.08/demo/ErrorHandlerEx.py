a = 10

try:
    b = int(input("Введите знаменатель: "))
    c = a/b
    #print(c)
##except ValueError as e:             # Получение информации об исключении
##    print("Преобразование прошло неудачно", e)
#except ZeroDivisionError as e:
#    print("Error - деление на нуль", e)
except Exception as ex:
    print("Error!", ex)    
else:
    print(c)
