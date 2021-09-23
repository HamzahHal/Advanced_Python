class User:
    def sign_in(self):
        user = input('Enter Username: ')
        password = input('Enter Password: ')
        accessUser = 'Logged In' if user == 'Hal' else 'Try Again'
        accessPass = 'Logged In' if password == 'letmein' else 'Try Again'
        if accessUser and accessPass:
            print(accessUser)


class Wizard(User):
    def __init__(self, name, element):
        self.name = name
        self.element = element

    def attack(self):
        print(f'Attacking with {self.element}')


wizard1 = Wizard('Dr. Strange', 'Fire')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        attack_num = int(input('Enter amount of arrows you want to shoot: '))
        arrow_left = self.arrows - attack_num
        print(f'Attacking with {attack_num} arrows, you now have {arrow_left} arrows left ')


Archer1 = Archer('Green Arrow', 100)


print(wizard1.sign_in())

print(Archer1.attack())
