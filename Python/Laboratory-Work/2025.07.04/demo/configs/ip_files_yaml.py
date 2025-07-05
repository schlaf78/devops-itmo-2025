import yaml
from pathlib import Path

# Ansible inventory
data = yaml.safe_load(Path('inventory.yaml').read_text())

hosts = data['all']['hosts']
for host, info in hosts.items():
    ip = info.get('ansible_host')
    if ip:
        print(f"{host}: {ip}")


# Kubernetes pod config
data = yaml.safe_load(Path('pod.yaml').read_text())

ip = data.get('spec', {}).get('nodeIP')
if ip:
    print(f"Pod запущен на IP: {ip}")
