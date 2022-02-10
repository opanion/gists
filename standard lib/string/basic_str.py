import string

##string constants
#print(string.ascii_letters)
#print(string.digits)
#print(string.hexdigits)
#print(string.punctuation)

#use constants to filter string
string1 = 'A cow is an animal with 4 chambers in their stomach'
string2 = 'Supercalifragralistic'
string3 = '9484492'

#print(''.join([s for s in string1 if s in string.ascii_letters]))

print(string1.isnumeric())
print(string3.isnumeric())

