class User:
    @staticmethod
    def sign_in():
        user = input('Enter Username: ')
        password = input('Enter Password: ')
        accessUser = 'Logged In' if user == 'Hal' else 'Try Again'
        accessPass = 'Logged In' if password == 'letmein' else 'Try Again'
        if accessUser and accessPass:
            print(accessUser)

    # accessing this method through the Wizard attack method
    def attack(self):
        print('do nothing')


# Here I inherit the User class and this becomes a sub class
class Wizard(User):
    def __init__(self, name, element):
        self.name = name
        self.element = element

    def attack(self):
        # Here is where I'm accessing the main parent classes method
        # Polymorphism
        User.attack(self)
        print(f'Attacking with {self.element}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'{self.name} is beginning their attack, be prepared!')
        attack_num = int(input('Enter amount of arrows you want to shoot: '))
        if attack_num <= self.arrows:
            arrow_left = self.arrows - attack_num
            print(f'Attacking with {attack_num} arrows, you now have {arrow_left} arrows left ')
        else:
            print(f"I'm sorry {self.name}, you don't have enough arrows to make this attack. Currently you only hold {self.arrows}")
        self.arrows = arrow_left


# Instantiated objects
wizard1 = Wizard('Dr. Strange', 'Fire')

archer1 = Archer('Green Arrow', 100)


# Polymorphism
def player_attack(char):
    char.attack()


# Polymorphism
for char in [wizard1, archer1]:
    char.attack()
print(wizard1.attack())
# player_attack(wizard1)
# player_attack(wizard1)
# player_attack(archer1)
# wizard1.attack()
# archer1.attack()
# print(archer1.arrows)
# print(isinstance(wizard1, object))
