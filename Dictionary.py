# Dictionary
x, y, z = {'car': 45, 1: 'new', 'carbon': 32}

# homer = 'never'
# x = {'never': 'ever'}
print(type(y))
new_type = str(y)
print(new_type)
print(type(new_type))

dictionary_items = {
    'a': [1, 5, 6],
    'b': 2,
    'c': 3
}
print(dictionary_items['a'][1])

new_list = [
    {
        'a': [1, 5, 6],
        'b': 2,
        'c': 3
    },
    {
        'f': [6, 2, 0],
        'k': 2,
        'l': 3
    }
]
print(new_list[1])
print(new_list[1]['f'])
print(new_list[1]['f'][0])

# Use the get method in order to find values from keys in a dictionary so it doesn't break the rest of the code execution
print(new_list[0].get('a', 'The value doesnt exist'))

user = {
    'basket': [1, 3, 4],
    'greet': 'jello',
    'age': 30
}

print('basket' in user)
print('size' in user)
print(user.update({'age': 55}))
print(user)