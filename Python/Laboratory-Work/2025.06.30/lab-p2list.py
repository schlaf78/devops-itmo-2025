#1
List1 = [82,8,23,97,92,44,17,39,11,12]
print("Original Array:",List1)
#2
#print(dir(List1))
#3
#print(help(List1.insert))
#print(help(List1.append))
#print(help(List1.sort))
#print(help(List1.remove))
#print(help(List1.reverse))
#4
for i in range(len(List1)):
    List1[i] += 5
print("Editied Array:",List1)
#5
List1.extend([100])
print("1 added at the End item in Array:",List1)
#6
List1.insert(4, 200)
print("1 added item in custom place in Array:",List1)
#7
List1.pop(0)
print("Delete 1st item in Array:",List1)
#8
List1.pop(-1)
print("Delete last item in Array:",List1)

#Array sorting
#1
List1.sort(reverse=True)
print("Sorted array by descending",List1)
#3
List2 = [3,5,6,2,33,6,11]
Lis = sorted(List2)
print("Sorted array by ascending",Lis)

#Tuple
#1
#print("Help for dor of tuple:",dir(tuple))
#2
print("Help for tuple.index:",dir(tuple.index))
print("Help for tuple.count:",dir(tuple.count))
#3
Seq = (2,8,23,97,92,44,17,39,11,12)
#4
print(Seq.count(8))
print(Seq.index(44))
#5
Listseq = list(Seq)
print(Listseq)
#6
print(type(Listseq))

#Vocabularies
#1
D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
#2
print(D['food'])
D['quantity'] += 10
print(D['quantity'])
#3
Dp = ()
Name = input("Enter name:")
Age = input("Enter age:")
print(Dp + (Name, Age))

#Nesting
#1
Rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'},
'job': ['dev', 'mgr'],
'age': 25
}
#2
print(Rec['name']['firstname'])
print(Rec['job'])
#3
Rec['job'].append('janitor')
Rec['job'].append('cleaner')
#4
FullName = Rec['name']['firstname'] + ' ' + Rec['name']['lastname']
Jobs = ', '.join(Rec['job'])
Age = Rec['age']

print(FullName, Age, Jobs)