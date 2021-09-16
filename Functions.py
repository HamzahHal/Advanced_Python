# # DRY
# # (Positional) Parameters
# def say_hello(name, emoji):
#
#     print(f'hello {name} {emoji}')
#
# # Positional Arguments
# name = input("Enter your name: ")
# emoji = input("Enter your emoji: ")
#
# say_hello(name, emoji)
# say_hello(emoji, name)
#
# # Keyword arguments
# say_hello(emoji=':D', name="bibi")

# Default Parameters - allow us to give definig the function a default value to the parameter/ variable
def default_say_hello(name='Darth Vader', emoji='XD'):

    print(f'hello {name} {emoji}')

default_say_hello()
default_say_hello('Collin')

def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)

# A function should do one thing really well. (it's ok to do multiple things as well though)
# Should return something
# print(sum(15,65))

totale = sum(10, 20)
print(totale)