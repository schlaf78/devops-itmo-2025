'''подсчет количества файлов каждого типа в текущем каталоге'''
from pathlib import Path
from collections import Counter
from datetime import datetime

k1 = Counter(path.suffix for path in Path.cwd().iterdir())
k2 = Counter(path.suffix for path in Path.cwd().glob("*.p*")) # файлы с суффиксом .p
print(k1, k2)



import os
'''показано, как получить время последнего изменения файлов.
Вывод в секундах и размер файла'''
with os.scandir(Path.cwd()) as dir_contents:
    for entry in dir_contents:
       info = entry.stat()
       print(info.st_mtime, info.st_size)

'''Создание каталога
Если каталог уже существует, os.mkdir() вызывает FileExistsError'''
try:
    os.mkdir('example_directory_os/')
except FileExistsError as exc:
    print(exc)

'''создать группу каталогов типа employees/managers/sales'''
os.makedirs('employees_os/managers/sales', exist_ok=True)

'''модуль для сопоставления шаблонов — glob
glob.glob('*.py')ищет все файлы с .py расширением в текущем каталоге и
возвращает их в виде списка.
Glob также поддерживает подстановочные знаки в стиле оболочки для соответствия шаблонам'''
import glob
for name in glob.glob('*[0-9]*.py'):
    '''будут найдены все .py-файлы, имена которых содержат цифры'''
    print('glob', name)

'''составить список всех файлов и каталогов в дереве каталогов с помощью os.walk()
os.walk()по умолчанию перемещается по каталогам сверху вниз.
Чтобы пройти по дереву каталогов снизу вверх, передайте topdown=False '''
for dirpath, dirnames, files in os.walk('.', topdown=False):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name)


'''Модуль pathlib имеет соответствующие методы.

Получение информации о файле, которые дают одинаковые результаты,
добавлено преобразование секунд в datetime'''

current_dir = Path(Path.cwd())
for path in current_dir.iterdir():
    info = path.stat()
    print(path.name, datetime.utcfromtimestamp(info.st_mtime).strftime('%d %b %Y'),
          info.st_size, sep='--\t')

'''Создание каталога
Если каталог уже существует, mkdir() вызывает FileExistsError'''
p = Path('example_directory_path/')
p.mkdir(exist_ok=True)

'''создать группу каталогов'''
p = Path('employees_path/managers/sales')
p.mkdir(parents=True, exist_ok=True)

'''составить список типов файлов, начинающихся с буквы p, имена которых содержат цифры'''
p = Path('.')
for name in p.glob('*[0-9].p*'):
    print(name)




