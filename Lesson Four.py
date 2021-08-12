# Escape Sequence
weather = "it's a sunny \"day\"" \
          "\nhope you have a good day"

print(weather)
# Formatted String
name = 'Galvin'
age = 23

print(f'hi {name}. you are {age} years old')
print('hi {}. you are {} years old'.format(name, age))
print('hi {name_new}. you are {age} years old'.format(name_new='Jonah', age=120010))


selfish_thing = '01234567'
               # 01234567
print(selfish_thing[0])

selfish_thing += '8'

print(selfish_thing)


print(len(selfish_thing))

quote = 'to be or not to be'

test = quote.find('j')
if test < 0:
    print('not found myguy')
else:
    print('Found it myguy')

print(quote)
print(test)