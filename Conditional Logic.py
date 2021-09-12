is_old = True
is_license = False

if is_old & is_license:
    print("you may drive with age & license !")
elif is_license:
    print("You have a license but not the age")
elif is_old:
    print("You have the age but not the license")
else:
    print("you may not drive yet")

print("testertester")

is_age = 20
is_name = 'henry'
if is_age > 10:
    print("you're old")
    
# Ternary Operator
# condition_if_true if condition else condition_if_else
is_friend = True
can_message = 'Message Allowed' if is_friend else "Not Allowed To Message"

print(can_message)


name = 'Hamzah'
correct_name = 'Name Correct' if name == 'Hamzah' else 'Incorrect Name'

print(correct_name)

# Short Circuiting
is_buddy = True
is_user = True
if is_buddy or is_user:
    print("best friends forever!")

# Logical Operators
# and
# or
# not
# print(4 < 5)
# print(3 > 6)
# print(3 == 3)
# print(3 != 0)
# print('a' > 'A')
# print(not(1 == 2))

is_magician = True
is_expert = False
# check if magician AND expert: ' you are a master magician.
# check if magician but not expert: ' at least you're getting there '

# if you're not a magician: "you need magic powers".

if is_magician & is_expert:
    print('You are a master magician')
elif is_magician and not is_expert:
    print("you're getting there")
elif not is_magician:
    print('You need magic power')

print(True is True)
print('1' is '1')
print([] is [])
print(10 is 10)
a = [1,2,3]
b = [1,2,3]
print(a == b)


