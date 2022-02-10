from string import Template

the_str = 'The quick brown $animal $action over the lazy dog'
template = Template(the_str)
keys = {'animal': 'lion', 'action':'ran'}
output_str = template.substitute(keys)

print(output_str)