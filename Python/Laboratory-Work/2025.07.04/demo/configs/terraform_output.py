import json
from pathlib import Path

data = json.loads(Path('terraform_output.json').read_text())

for name, entry in data.items():
    ip = entry.get("value")
    if ip:
        print(f"{name}: {ip}")
