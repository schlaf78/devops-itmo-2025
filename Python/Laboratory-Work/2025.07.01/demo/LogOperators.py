# falsy объекты
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool(''))
print(bool({}))

#truthy объекты
print(bool(True))
print(bool(123))
print(bool(69.96))
print(bool('beegeek'))
print(bool([4, 8, 15, 16, 23, 42]))
print(bool({1, 2, 3}))

data = [1,3]
value = 12
if len(data) > 0:
    ...

if value == True:
    ...

if value == False:
    ...

if data:
    ...  

if value:
    ...  

if not value:
    ...

print(None or 0)
print(0 or 5)
print('beegeek' or None)
print([1, 2, 3] or [6, 9])

print(1 or 'beegeek' or None)
print(0.0 or 'hab' or {'one': 1})
print(0 or '' or [6, 9])
print(0 or '' or [])
print(0 or '' or [] or {})

print(None and 10)
print(5 and 0.0)
print('beegeek' and {})
print([1, 2, 3] and [6, 9])

print(1 and 'beegeek' and None)
print('hab' and 0 and {'one': 1})
print(10 and [6, 9] and [])


a = 5
b = 10
c = 15

print(a < b < c)        # True    
print(a < b and b < c)  # True

lst = [1,2, 3]
num = 2

print(num in lst == True) #False
print(num in lst and lst == True)

