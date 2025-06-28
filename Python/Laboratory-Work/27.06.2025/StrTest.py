# Строка - это упорядоченная неизменяемая последовательность символов Юникода

''' 1. Как склеить две строки? '''
x = str("AXTR")   # x станет 's1'  
y = str(567)      # y станет '2'
xy = x + y
print(xy)

''' 2. Как склеить три строки? 
join() — метод, позволяющий склеить N строк с произвольным разделителем
join() — это метод объекта «строка», принимающий в качестве аргумента список
и возвращающий на выходе новую строку '''
names = ["John", "Paul", "Ringo", "George"]
allNames = "; ".join(names)
print(allNames)         # John; Paul; Ringo; George

""" Задание: реализуйте свою реализацию метода join()"""

''' 3. Как разделить строку?
Метод split() - применяется к целевой строке, а разделитель передаётся аргументом
      обратите внимание на различие в применении join и split'''
st = "Мама, мыла раму"
stm = st.split(",")
print(stm)              # ['Мама', ' мыла раму']

''' срезы (slices)
Срез s[x:y] позволяет получить подстроку с символа x до символа y 
При помощи необязательного третьего параметра s[x:y:N] можно выбрать из подстроки каждый N-ый символ '''

#получить только символы на четных позициях:
s = "a123y56t89"
print(s[::2])               # a2y68
# получить только символы на нечётных позициях:
print(s[1::2])              # 135t9

# изменить первый символ
s = "Вася"
s = 'Т' + s[1:]
print("Был Вася, стал", s)



'''Поиск в строке
Простой поиск:
    Проверить, начинается ли (заканчивается ли) строка с выбранных символов. 
    Для этого в Python предусмотрены специальные строковые методы '''
s = "0123456789"
print(s.startswith("012"))          # True
print(s.endswith("69"))             # False

"""Для поискa подстроки в произвольном месте есть метод find() - вернет
       индекс начала найденного вхождения подстроки в строку,
       либо -1, если ничего не найдено """
s = "0123456789"
print(s.find("45"))                 # 4
print(s.find("42"))                 # -1

'''
Сложный поиск:
   Если нужно найти не конкретную последовательность символов, а некий шаблон, то - регулярные выражения
'''
import re
s = "http://itcenter.itmo.ru/inzhener_programmist_750";
result = re.match(r"^(http|https)://([^/]+)(.*)$", s)
print(result.group(1)) # http
print(result.group(2)) # itcenter.itmo.ru
print(result.group(3)) # /inzhener_programmist_750

'''
Замена в строке
    При помощи срезов и склейки строк можно заменить что угодно '''
s = "Hello, darling! How are you?"
s1 = s[:7] + "Василий" + s[14:]
print(s1)              # 'Hello, Василий! How are you?'
'''
   При помощи метода replace() '''
s2 = s.replace("darling", "Василий")
print(s2)              #'Hello, Василий! How are you?'
'''
    Любую проблему можно решить регулярными выражениями.
    В случае с заменой нужен метод re.sub() '''
s = "ttp://itcenter.itmo.ru/inzhener_programmist_750";
s3 = re.sub('[a-z]', 'Y', s)
print(s3)              # YYY://YYYYYYYY.YYYY.YY/YYYYYYYY_YYYYYYYYYYY_750

'''
    Форматирование строк
    Стандартная задача: сформировать строку, подставив в неё результат работы программы.
    Начиная с Python 3.6, это можно делать при помощи f-строк '''
sf = f"Строка '{s}' содержит {len(s)} символов."
print(sf)              # "Строка 'Hello, world!' содержит 13 символов."
'''
В более ранних версиях языка '''
sf1 = "Строка '%s' содержит %d символов" % (s, len(s))
sf2 = "Строка '{}' содержит {} символов".format(s, len(s))
print(sf1,'\n', sf2)


'''Шаблонизированные строки — механизм подстановки для строк, в частности для задач, где необходимы простые подстановки слов. 
В качестве подстановочного символа в них указан $ с необязательными фигурными скобками вокруг него.
Вставляемое значение задается символами, непосредственно следующими за $
подробне см. https://docs.python.org/3/library/string.html#template-strings
'''
# A Simple Python template example
from string import Template

# Create a template that has placeholder for value of x
t = Template('x is $x')

# Substitute value of x in above template
print (t.substitute({'x' : 1}))

greeting = Template("$hello Mark Anthony")
greeting.substitute(hello="Bonjour") # 'Bonjour Mark Anthony'
greeting.substitute(hello="Привет")  # 'Привет Mark Anthony'
greeting.substitute(hello="Nĭn hăo") # 'Nĭn hăo Mark Anthony'


# List Student stores the name and marks of three students
Student = [('Ram',90), ('Ankit',78), ('Bob',92)]

# We are creating a basic structure to print the name and
# marks of the students.
t = Template('Hi $name, you have got $marks marks')

for i in Student:
	print (t.substitute(name = i[0], marks = i[1]))

'''${Identifier} работает как $Identifier, но явно выделяет заполнитель''' 
template = Template( 'That $noun looks ${noun}y')
string = template.substitute(noun='Fish')
print(string)
# That Fish looks Fishy

''' Генерация исключения при несовпадении шаблону'''
s = Template('$who likes $what')
s.substitute(who='tim', what='kung pao') # 'tim likes kung pao'

d = dict(who='tim') 
Template('Give $who $100').substitute(d)
# Traceback (most recent call last):
# ...
# ValueError: Invalid placeholder in string: line 1, col 11

Template('$who likes $what').substitute(d)
# Traceback (most recent call last):
# ...
# KeyError: 'what'

''' а так исключения не будет, просто вывод''' 
Template('$who likes $what').safe_substitute(d) # 'tim likes $what'




