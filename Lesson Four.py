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