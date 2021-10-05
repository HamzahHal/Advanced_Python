from functools import reduce


def math_test(li):
    new_item = []
    trash_item = []
    for i in li:
        if 1 < i < 20:
            new_item.append(i)
        elif 1 > 1 == 5:
            trash_item.append(i)
    return new_item


print(math_test([1, 3, 2, 6, 9, 10, 20, 40, 5]))


def myfunc(n):
    return len(n)


x = map(myfunc, ('apple', 'banana', 'cherry'))

print(x)
print(myfunc('asdasdasd'))

li = [1, 3, 4, 5, 6, 34, 65, 95, 37, 32032, 3232, 320432, 6593, 349]


def list_filter(li):
    filtered_items = []
    for items in li:
        if 100 > items > 53:
            filtered_items.append(items)
    return filtered_items


print(list_filter(li))


def multiply_by2(lif):
    new_list = []
    for item in lif:
        new_list.append(item * 2)
    return new_list


print(multiply_by2([3, 10, 5]))

# Map, filter, zip and reduce

my_list = [1, 2, 3]
your_list = {10, 20, 30}
their_list = [5, 4, 3]


def multiply_by2_map(result):
    # result = list(map(my_list * 2, new_num))
    return result if result > 5 else 'nope'


item_div = [1, 3, 6, 5, 7, 8, 9, 9, 34, 432, 5434, 5434, 4, 353, 34]


def divide_map(item):
    return item / 2


# Filter
def only_odd(item):
    return item % 2 != 0


name1 = 'Hamzah', 'Galvin', 'Rav', 'Talha', 'Moh'


def user_filter(items):
    return items != 'Hamzah'


result_list = list(map(multiply_by2_map, my_list))
result_tuple = tuple(map(multiply_by2_map, my_list))
result_set = set(map(multiply_by2_map, my_list))
# The reason why it shows the memory location for this is because, map iterates over each item in the dataset but converting it to a string would mean that all the items are to
# become 1 whole string which is the reason why it won't show the result and instead only shows its memory location and that it's type has turned to a string.
result_string = str(map(multiply_by2_map, my_list))
print(result_list)
print(result_tuple)
print(result_set)
print(result_string)
print(type(result_string))

new_map = list(map(divide_map, item_div))
new_map_str = str(list(map(divide_map, item_div)))

print(type(new_map))
print(type(new_map_str))
print(new_map_str)
print(new_map)
print(list(filter(only_odd, my_list)))
print(list(filter(user_filter, name1)))


# Zip
# print(list(zip(my_list, your_list, their_list)))
# Reduce
def accumulator(acc, item):
    print(acc + item)
    return acc + item


print(reduce(accumulator, my_list, 10))

increase = 10, 10, 10


def baseExp(base, value):
    return base + value


print(reduce(baseExp, increase, 1))
current_exp = 0
for i in range(2):
    current_exp += reduce(baseExp, increase, 1)

print(current_exp)

characters = 'a', 'b', 'c', 'd'


def char_add(first, char):
    return first + char


print(reduce(char_add, characters, 'A'))
# print(multiply_by2(my_list))
# print(new_num)
