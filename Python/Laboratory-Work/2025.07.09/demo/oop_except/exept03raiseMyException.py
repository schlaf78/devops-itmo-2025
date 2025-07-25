# Базовым классом MyEx должен быть либо класс Exception, либо один из его наследников. 

class MyEx(Exception):
        def __init__(self, ind, mes):
            self.__ind = ind
            self.__mes = mes
        def __str__(self):
            #return "Указанное значение {} опасно".format(self.__ind)
            return str(self.__ind) + self.__mes        

def fun(obj, index):
    return obj[index]

x = "ABBA"
print(fun(x,3))
# print(fun(x,4)) # IndexError: string index out of range

while True:
    try:
        k = int(input("Введите индекс: "))
        if k == 0:
            raise MyEx(k, "При вводе в цикле")
        f = fun(x,k)
        break
    except MyEx as e:
        print('\nОпасная ошибка!', e)
    except ValueError as er:
        print('Внимание! ', type(er), er)
    except IndexError: # Перехватывает и обрабатывает исключение
        print('\nИндекс вне диапазона')
    except Exception as e:
        print('\nОшибка!', e)
    finally:
        print('Отключите питание')
    print('End loop')

print(f)

    
