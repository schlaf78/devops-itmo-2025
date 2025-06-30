#Моделирование бросания кубика
"""
Подключение модуля к программе выполняется с помощью оператора import
У него есть две формы: import и from-import
"""
import random           # импорт модуля
n1 = random.randint(1, 6)

import random as rnd    # импорт модуля как псевдонима
n2 = rnd.randint(1, 6)


from random import randint  # импорт функции
n3 = randint(1, 6)
randint = "проблема"


from random import *        # импорт всех функций модуля
n4 = randint(1, 6)

from random import randint as rnd   # импорт функции как псевдонима
#rnd = "fr" <== This one was incorrect before comment of this line
n5 = rnd(1, 6)


#n3 = randint

print('Выпало:', n1, n2, n3, n4, n5)

            
