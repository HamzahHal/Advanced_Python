# Lambda Expressions
from functools import reduce

# lambda param: action(param)

my_list = [1, 2, 3]

# def multiply_by2_map(result):
#     # result = list(map(my_list * 2, new_num))
#     return result * 2


result_list = list(map(lambda item: item * 2, my_list))

print(result_list)

print(list(filter(lambda item: item < 2, my_list)))
print(reduce(lambda acc, item: acc + item, (my_list + my_list)))

imput = 'hey'
carta = 'taker'
result = reduce(lambda acc, item: acc + item, (imput + carta))

print(result)


