# Data Types
int_type = 1
float_type = 1.2
bool_type = True
str_type = "Test"
list_type = list('dsa')
tuple_type = tuple("adsasda")
set_type = set('dsad')
dict_type = {13123: 323232,
             'no': 3203}

print(int_type)
print(float_type)
print(str_type)
print(list_type)
print(tuple_type)
print(set_type)
print(dict_type)

print(type(1))
print(type(2 - 4))
print(type(2 * 4))
print(type(2 / 4))  # 0.5
print(type(0.5343))

print(2 ** 3)
print(float(2 // 4))
# Return remainder of  the divided value
print(9 % 5)

# math functions
print(round(7.6))
print(round(3.2))
print(abs(-342))

# list - type of array (data type)
li = [1, 2, 3, 4, 5]
li2 = ['c', 'v', 'b']
li3 = [1.5, 3, 4.54, 's', False]
amazon_cart = ['notepad', 'testcare']
print(amazon_cart[0])
new_value = 'test'
new_value2 = 'fello'
amazon_cart.insert(1, 'testewr')
amazon_cart.append(new_value)
amazon_cart.append([new_value, new_value2])
print(amazon_cart)

new_cart = [
    'notework',
    'sunglasses',
    'toys',
    'grapes',
    'shoes'
]
new_cart[0] = 'Laptop'
# duplicate instead of just changing
# simply assigns list to a new variable name - newer_cart = new_cart
newer_cart = new_cart[:]
newer_cart[0] = 'Gumo'
print(newer_cart)
print(new_cart)

# Matrix
matrix = [
    [1, 2, 3],
    [3, 4, 5],
    [7, 8, 9]
]

print(matrix[0][1])
for num in matrix:
    print(num)

# Adding
basket = [1, 2, 3, 4, 5]
new_item = basket[:]
new_item.insert(0, 100)
new_item.extend([1000, 10001])
print(basket)
print(new_item)

# removing
basket.remove(1)
print(basket)
basket.pop()
print(basket)
basket.pop(2)
print(basket)

# Index Locator
cart = ['f', 'k', 'x', 'i', 's']
user_id = ['k', 'player']
print(cart.index('x', 0, 3))
print('l' in cart)
print('x' in cart)

# cart.sort()
new_cart = sorted(cart)
new_cart.reverse()
print(new_cart)
# print(sorted(cart))
print(cart)
# tries = 3
# for x in range(tries):
#     for user_id[1] in cart:
#         print('true')
#         break
#     else:
#         print('false')
#         break


letters = ['a', 'x', 'v', 's', ' b', ' f']

# Using range to create a list up to the range amount
number_range = list(range(50))

print(number_range)

new_sentence = ' '.join(['Hi', 'Name', 'is', 'Hamzah'])

print(new_sentence)

# List Unpacking
a, b, c, *other = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)
print(type(other))
# print(d)

x, y, z = {'car': 45, 1: 'new', 'carbon': 32}

# homer = 'never'
# x = {'never': 'ever'}
print(type(y))
new_type = str(y)
print(new_type)
print(type(new_type))

# Dictionary
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

# Game data storage using a dictionary inside a list
Player_Data = [
    {
        'Player Name': 'K1LL3R101',
        'Age': 2500,
        'Base Health': 100,
        'Additional Health': 0,
        'Items Equippable': 5,
        'Items Equipped': ['Sword', 'Gun', 'Spear']
    },
    {
        'Player Name': 'TaleOfScripting',
        'Age': 53443,
        'Base Health': 100,
        'Additional Health': 433,
        'Items Equippable': 58,
        'Items Equipped': 34,
    }
]

print(Player_Data[0]['Player Name'])

Player_Data[0]['Player Name'] = 'VetexGames'
Player_Data[1]['Player Name'] = 'ShadeOfAzure'


print(Player_Data[0]['Items Equipped'])
print(Player_Data[1]['Player Name'])
print(Player_Data[1]['Age'])

Item_len = len(Player_Data[0]['Items Equipped'])
print(Item_len)

slots_left = Player_Data[0]['Items Equippable'] - Item_len
print(slots_left)

if Item_len < Player_Data[0]['Items Equippable']:
    print(f'You have {slots_left} equip slots left')

# Classes -> custom types


# Specialized Data Types
# Modules
