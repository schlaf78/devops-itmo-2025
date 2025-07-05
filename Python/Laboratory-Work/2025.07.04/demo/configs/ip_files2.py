'''
Извлечение параметров из конфигов'''
from pathlib import Path

import re

for line in Path('file01.cfg').read_text().splitlines():
    match = re.search(r'ip address (\d+\.\d+\.\d+\.\d+)', line)
    if match:
        print("Найден IP:", match.group(1))


