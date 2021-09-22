# OOP


class PlayerCharacter:
    # Class object attribute (static , not dynamic)
    membership = True

    def __init__(self, name='Anonymous', age=0):
        if age > 18:
            self.name = name  # Attributes
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    def run(self, hello):
        print(f'name name name {self.name}')


#player1 = PlayerCharacter('collu', 50)
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

#print(player1.run('hiiiiiiiiiiiiiii'))
# print(f'attack {player2.attack}')
# # print(f'speed {player2.speed}')
# print(f'health {player2.health}')
# # print(f'power {player2.power}')
#print(player2.membership)
#print(player1.shout())
print(player2.attack)
print(player2.name)
