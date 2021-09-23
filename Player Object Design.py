# Can we make this private
# OOP
class PlayerCharacter:
    # Class object attribute (static , not dynamic)
    membership = True

    def __init__(self, name='Anonymous', age=0):
        if age > 18:
            self._name = name  # Attributes
            self._age = age

    def run(self):
        return self

    def speak(self):
        print(f'my name is {self._name} & I am {self._age} years old')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Terry', num1 + num2)

    @staticmethod
    def adding_more_things(num1, num2):
        return num1 + num2

    @property
    def name(self):
        return self._name


player1 = PlayerCharacter('collu', 50)
player2 = PlayerCharacter('Tom', 43)
player2.attack = 50
player2.speed = 34
player2.health = 10000
player2.power = 436
player2.expBar = 0
player2.expMax = 100
player2.expCount = 0
player2.hit = False
# x = int(input("Enter Value: "))
# if x > 1:
#     player2.hit = True
#
# if player2.hit:
#     player2.expCount += 1
#
# if player2.expCount > 0:
#     player2.expBar += 100
#
# if player2.expBar == player2.expMax:
#     player2.health += (60 / 2)
#     player2.attack += (100 / 2)

# print(player1.run('hiiiiiiiiiiiiiii'))
# print(f'attack {player2.attack}')
# # print(f'speed {player2.speed}')
# print(f'health {player2.health}')
# # print(f'power {player2.power}')
# print(player2.membership)
# print(player1.shout())
player3 = PlayerCharacter.adding_things(12, 3)
# print(player3.run)

# Example of a Dunder Method
# __doc__
print(help.__sizeof__())
print(player1.name)
