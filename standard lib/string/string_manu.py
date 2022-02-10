import string

str1 = 'The quick brown fox jumps over the lazy dog on the 1st of December'
print(str1.upper())
print(str1.lower())

#split_str = str1.split(' ')
#print(split_str)
letters = 'abcdefgh'
join_str = ', '.join(letters)
print(join_str)

names =['Amy', 'Jewel', 'Dada', 'Nii', 'James', 'Michael']
biggest = max([len(name) for name in names])

for name in names:
    print(name.ljust(biggest+2, '-') + ':')

for name in names:
    print(name.center(biggest+2, '-') + ':')

for name in names:
    print(name.rjust(biggest+2, '-') + ':')