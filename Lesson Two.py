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
# li = [1, 2, 3, 4, 5]
# li2 = ['c', 'v', 'b']
# li3 = [1.5, 3, 4.54, 's', False]
# amazon_cart = ['notepad', 'testcare']
# print(amazon_cart[0])
# new_value = 'test'
# new_value2 = 'fello'
# amazon_cart.insert(1, 'testewr')
# amazon_cart.append(new_value)
# amazon_cart.append([new_value, new_value2])
# print(amazon_cart)

new_cart = [
    'notework',
    'sunglasses',
    'toys',
    'grapes',
    'shoes'
]
new_cart[0] = 'Laptop'
# duplicate instead of just changing
newer_cart = new_cart
newer_cart = new_cart[:]
newer_cart[0] = 'Gumo'
print(newer_cart)
print(new_cart)

# Matrix
matrix = [
    [1,2,3],
    [3,4,5],
    [7,8,9]
]

print(matrix[0][1])
for num in matrix:
    print(num)

# Adding
basket = [1,2,3,4,5]
new_item = basket[:]
new_item.insert(0,100)
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

# Classes -> custom types


# Specialized Data Types
# Modules
None
