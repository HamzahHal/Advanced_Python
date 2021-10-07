# Square
my_list = [5, 4, 3]

result = list(map(lambda item: item * item, my_list))

print(result)

# List Sorting
a = [(0, 2), (4, 3), (10, -1), (9, 9)]
a.sort(key=lambda x: x[1])
print(a)
