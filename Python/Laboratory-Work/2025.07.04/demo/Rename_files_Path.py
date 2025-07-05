'''
Автоматическое переименование'''

from pathlib import Path

folder = Path(Path.cwd())

# Получаем все файлы .png и .jpeg (без учёта регистра)
image_files = sorted([f for f in folder.iterdir() if f.suffix.lower() in ['.png', '.jpeg']])

# Переименовываем файлы по шаблону image_N.расширение
for idx, file in enumerate(image_files, start=1):
    new_name = f"image_{idx}{file.suffix.lower()}"
    new_path = folder / new_name
    file.rename(new_path)
    print(f"{file.name} → {new_name}")
