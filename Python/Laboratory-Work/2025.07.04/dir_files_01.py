''' 1. Создание новой директории m_folder '''
#import shutil
#import os
from pathlib import Path # Модуль предоставляет объектно-ориентированный API для работы c путями файловой системы

home = Path.home()
print(home)

my_folder = home / "my_folder"  # оператор / для расширения пути
print(my_folder)

if not my_folder.exists():
    my_folder.mkdir()

my_folder.mkdir(exist_ok=True)

''' 2. Добавление файлов в директорию'''
file1 = my_folder / "file1.txt"
file1.touch()     # первый способ
(my_folder / "file2.txt").touch()    # второй способ
my_folder.joinpath("image.png").touch()    # третий способ

       
''' 3. Перемещение файла с изображением в новый каталог '''

''' 3.1 создание нового каталога внутри my_folder'''
if not (my_folder / "images").exists():
    (my_folder / "images").mkdir()

(my_folder / "images").mkdir(exist_ok=True)
''' 3.2 перемещение файла изображения в созданный каталог '''
#path_destination = my_folder / 'images'

'''
for f in my_folder.glob('*.png'):    # отбор файлов по шаблону
    print(shutil.which(f)) # находит полный путь к файлу c указанным именем
    shutil.move(os.path.join(my_folder, f), path_destination)
    print(shutil.which(f)) # возвращает значение None'''

for f in my_folder.glob('*.png'):    # отбор файлов по шаблону
    path_destination = Path(my_folder /"images") / f.name
    f.replace(path_destination)

for file_path in my_folder.glob("*.txt"):
    print(file_path)
    new_path = Path(my_folder / "archive") / file_path.name
    file_path.replace(new_path)
