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

my_list = [1, 25, 3]
new_num = []


def multiply_by2_map(result):
    # result = list(map(my_list * 2, new_num))
    return result if result > 5 else 'nope'


item_div = [1, 3, 6, 5, 7, 8, 9, 9, 34, 432, 5434, 5434, 4, 353, 34]


def divide_map(item):
    return item / 2


result = list(map(multiply_by2_map, my_list))
print(result)
new_map = list(map(divide_map, item_div))
new_map_str = str(list(map(divide_map, item_div)))
change_map = float(new_map_str)

print(type(new_map))
print(type(new_map_str))
print(type(change_map))

print(new_map)
# print(multiply_by2(my_list))
# print(new_num)

