# Объекты языка Python должны
# записываться в файл только в виде строк

X, Y, Z = 43, 44, 45 
S = 'Spam' 
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

F = open('datafile.txt', 'w')           # Создает файл для записи
F.write(S + '\n')                       # Строки завершаются символом \n
F.write('%s,%s,%s\n' % (X, Y, Z))       # Преобразует числа в строки
F.write(str(L) + ';' + str(D) + '\n')   # Преобразует и разделяет символом ;
#F.write(X)
F.close()

# обратные преобразования, чтобы получить
# из строк в текстовом файле действительные объекты

F = open('datafile.txt')    # Открыть файл 
line = F.readline()         # Прочитать одну строку
line.rstrip()               # Удалить символ конца строки
print(line)                 # Spam 


line = F.readline()         # Следующая строка из файла
print(line)
# Это - строка ‘43,44,45\n’
parts = line.split(',')     # Разбить на подстроки по запятым
print(parts)
numbers = [int(P) for P in parts] # Преобразовать весь список в числа
print(numbers)

# преобразовать список и словарь

line = F.readline() # “[1, 2, 3];{‘a’: 1, ‘b’: 2}\n”
parts = line.split(';') # Разбить на строки по символу 
print(parts)

eval(parts[0])              # Преобразовать строку в объект
objects = [eval(P) for P in parts] # Преобразование для всех строк в списке
print(objects) # список включает список и словарь
