# OOP
def run():
    print('run')
    return 'Done'


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age


player1 = PlayerCharacter('Hamzah', 22)
player2 = PlayerCharacter('Tom', 55)
player2.attack = 50
player2.speed = 34
player2.health = 10000
player2.power = 436
player2.expBar = 0
player2.expMax = 100
player2.expCount = 0
player2.hit = False
x = int(input("Enter Value: "))
if x > 1:
    player2.hit = True

if player2.hit:
    player2.expCount += 1

if player2.expCount > 0:
    player2.expBar += 100

if player2.expBar == player2.expMax:
    player2.health += (60 / 2)
    player2.attack += (100 / 2)

# print(run())
print(f'attack {player2.attack}')
# print(f'speed {player2.speed}')
print(f'health {player2.health}')
# print(f'power {player2.power}')
