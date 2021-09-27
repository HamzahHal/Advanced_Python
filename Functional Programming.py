def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return new_list


print(multiply_by2([3, 10, 5]))


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
