days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
daysFr = ['Dim', 'Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam']

#use iter to create an iterable
i = iter(days)
print(next(i))
print(next(i))
print(next(i))

#use iter to readlines
with open('testfile.txt', 'r') as f:
    for i in iter(f.readline, ''):
        print(i)

#use enumerate to generate an index
for index, value in enumerate(days, start=1):
    print(index, value)

#use zip to combine two iterables
for i, m in enumerate(zip(days, daysFr), start=1):
    print(i, m[0], '=', m[1], ' in French')