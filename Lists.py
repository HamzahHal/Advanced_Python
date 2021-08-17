
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