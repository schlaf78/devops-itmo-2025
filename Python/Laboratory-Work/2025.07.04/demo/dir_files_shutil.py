'''Копирование, перемещение и переименование файлов и каталогов'''
import shutil

'''Чтобы скопировать файл из одного места в другое с помощью shutil.copy():'''

src = 'text.txt'
dst = 'employees_os'
shutil.copy(src, dst)

'''shutil.copy() копирует только содержимое файла и разрешения файла.
Другие метаданные, такие как время создания и изменения файла, не сохраняются.
Чтобы сохранить все метаданные файла при копировании, используйте shutil.copy2()'''

'''shutil.copytree()копирует весь каталог и все, что в нем содержится'''

shutil.copytree('employees_os', 'data_emp_backup')

'''Чтобы переместить файл или каталог в другое место'''
shutil.move('data_emp_backup', 'data_emp_backup_ar')

'''Если каталога назначения не существует, каталог-источник будет
переименован в имя каталога назнаяения'''

'''Или ---- переименование файлов и каталогов'''
import os
os.rename('data_emp_backup_ar', 'data_emp_backup_ar_rename')
'''Или '''
from pathlib import Path
data_file = Path('text_data.txt')
data_file.rename('data.txt')

'''создать архив TAR,ZIP используя shutil'''

# shutil.make_archive(base_name, format, root_dir)
shutil.make_archive('data_emp_backup_ar_rename_tar', 'tar', 'data_emp_backup_ar_rename')

'''извлечь архив:'''
shutil.unpack_archive('data_emp_backup_ar_rename_tar.tar', 'extract_data_emp_backup_ar_rename_tar/')
