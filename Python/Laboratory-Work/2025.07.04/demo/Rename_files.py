'''
Автоматическое переименование'''
import os
from pathlib import Path

folder = Path(Path.cwd())

for index, filename in enumerate(os.listdir(folder), start=1):
    if filename.endswith(".png"):
        new_name = f"pattern_{index:01}.png"
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
