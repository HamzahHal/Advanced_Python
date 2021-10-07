# List, Set, Dictionary

new_list = 'helloooooya'
my_list = [char for char in new_list]
my_list2 = [i for i in range(0, 100)]
my_list3 = [i * 2 for i in range(0, 100)]
# Generate list of even numbers
my_list4 = [i ** 2 for i in range(0, 100) if i % 2 == 0]
# Set and dictionary
my_list5 = {char for char in new_list}
my_list6 = {i for i in range(0, 100)}

simple_dict = {'a': 1,
               'b': 2}
my_dict = {key: value ** 2 for key, value in simple_dict.items() if value % 2 == 0}
new_dict = {key.join('ad'): value for key, value in simple_dict.items()}

other_dict = {num:num*2 for num in [1, 2, 3]}

print(other_dict)

# print(my_list)
# print(my_list2)
# print(my_list3)
# print(my_list4)
# print(my_list5)
# print(my_list6)
print(my_dict)
print(new_dict)
