'''
Автоматическое удаление устаревших логов'''
import time
from pathlib import Path

folder = Path(Path.cwd())
now = time.time()
cut_off = now - 86400  # 86400 секунд = 1 день

for file in (folder/"artifacts").glob('*.log'):
    if file.stat().st_mtime < cut_off:  # старше суток
        file.unlink()
        print(f"Удалён: {file}")

