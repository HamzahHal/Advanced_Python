# for item in 'Zero to Mastery':
#     print(item)
#
# for item in range(10):
#     print(item)
#
# for item in (1,2,3,4,5):
#     print(item)
#
# for item in {1,2,3,4,5}:
#     print(item)
#
# for item in [1,2,3,4,5]:
#     print(item)
#     item += 1
#     print(item)

# user = {
#     'name' :  'Golem',
#     'age': 2200,
#     'can_swim': False
#
# }
#
# for key, value in user.items():
#    print(key, value)
#
# for item in user.values():
#     print(item)
#
# for item in user.keys():
#     print(item)


# for item in (1,2,3,4,5):
#     for x in ['a','b','c']:
#         print(item, x)
# Iterables -> list, dictionary, tuple, set , string, range
# Iterated -> one by one to check each item in the collection
print("hellow world")

# Counter
# my_list = [1,2,3,4,5,6,7,8,9,10]
# counter = 0
#
# for items in my_list:
#     counter += items
#
# print(counter)

# for _ in range(10):
#     print(_)
#
# for _ in range(0, 10, 2):
#     print(_)
#
# for _ in range(10, 0, -1):
#     print(_)
#
# # using iterable to print a range as a list
# for _ in range(2):
#     print(list(range(10)))

# enumerate
# for i, char in enumerate('Helloooo'):
#     print(i, char)
#
#
# for i, char in enumerate([1,2,3,4,5]):
#     print(i, char)


# for i, char in enumerate((1,2,3,4,5)):
#     print(i, char)

# for i, char in enumerate(list(range(100))):
#     print(i, char)
#     if char == 50:
#         print(f'index of 50 is {i}')
#
# # While loops
# i = 0
# while i < 50:
#     i += 1
#     print(i)
# else:
#     print('done with all the work')
# #
# my_list = [1,2,3]
# for item in my_list:
#     print(item)
#
# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i += 1
#
# while True:
#     response = input('say something: ')
#     if response == 'Bye':
#         break

my_list = [1,2,3]
for item in my_list:
    continue
    print(item)

i = 0
while i < len(my_list):
    i += 1
    continue
    print(my_list[i])


my_list = [1,2,3]
for item in my_list:
    # still thinking
    pass

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    pass













# tries = 0
# attempts = 3
# username = 'Hamzah'
# password = 'letmein'
# while tries < attempts:
#     response = input('Enter Username: ')
#     response_pass = input('Enter Password: ')
#     if response == username and response_pass == password:
#         print('Sign in Successful')
#         break
#     else:
#         print('Try Again')
#         tries += 1
#         if tries >= attempts:
#             print("You've exceeded your daily attempts, try again next time")
