from collections import namedtuple

def get_name():
    for name in full_name:
        return True, result
    else: 
        return empty_tuple


full_name = namedtuple('name', ['First', 'Middle', 'Last'])
name = full_name('John', 'XYZ', 'Doe')
empty_tuple = ()
result = name.index("XYZ")

print(name, result)