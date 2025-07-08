mac = ['aaaa:cc80:7000']

res = []
for m in mac:
    res.append(m.replace(':', '.'))

print(res)
