from datetime import datetime
from time import strftime

#create datetime for today
today = datetime.now()
#print various day and month formatting
print(today.strftime('%a, %A %w %d'))

print(today.strftime('%b, %B %m'))
#print various time formating
print(today.strftime('%H, %I %M %S %p'))
#locale-specific
print(today.strftime('%c'))
print(today.strftime('%X'))
#short date format m/d/y

print(today.strftime('%m/%d/%y'))

#long date format day, day no, month, year
print(today.strftime('%A %w %M %Y'))

