from pathlib import Path
from sys import argv

if len(argv) < 2:
    print("Search catalog not specified.")
    print("Usage example: python <move_texts.py> <folder name>")
    exit(1)

destination_dir = argv[1]
current_dir = Path.cwd()
destination_dir = current_dir / destination_dir
destination_dir.mkdir(exist_ok=True)

for txt_file in current_dir.glob("*.txt"):
    if txt_file.is_file():
        destination = destination_dir / txt_file.name
        txt_file.replace(destination)