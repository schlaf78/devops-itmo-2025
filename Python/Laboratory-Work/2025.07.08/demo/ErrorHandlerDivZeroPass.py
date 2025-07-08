a = 10

try:
    b = int(input("Введите знаменатель: "))
    c = a/b
    print(c)
except ValueError as e:             # Получение информации об исключении
    print("Преобразование прошло неудачно", e)
except ZeroDivisionError: # проигнорировал ошибку
    pass
except Exception as ex:
    print("Error!", ex)    
else:
    print(c)


'''Пример применения'''
lst = [4, 2, 0, -1, -6]
for j in lst:     
    try:
       print(1/j)  
    except ZeroDivisionError:
      pass
