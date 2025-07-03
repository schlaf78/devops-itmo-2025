


d = (10, 'cat', [1,2,3])

print(d)

nd = d
print(nd)

id(d), id(nd)
print(id(d) == id(nd))

nd[0] +- 1
print(nd)

nnd = d[:]
print(id(d), id(nnd))


asd = [1, 4, 6, 32, 24]
nasd = [i/2 for i in asd]
print(nasd)

#List Incliding aka spiskoboyue vklucheniye
asd = [1, 4, 6, 32, 24]
nasd = [i/2 for i in asd if i%2==0]
print(nasd)