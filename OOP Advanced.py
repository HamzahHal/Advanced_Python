class User:
    def __init__(self, email):
        self.email = email

    @staticmethod
    def sign_in():
        user = input('Enter Username: ')
        password = input('Enter Password: ')
        accessUser = 'Logged In' if user == 'Hal' else 'Try Again'
        accessPass = 'Logged In' if password == 'letmein' else 'Try Again'
        if accessUser and accessPass:
            print(accessUser)


class Wizard(User):
    def __init__(self, name, element, email):
        # Best method to access the Parent Class's __init__ constructor's attribute(email)
        super().__init__(email)
        # Alternative method to access the Parent Class's __init__ constructor's attribute(email)
        # User.__init__(self, email)
        self.name = name
        self.element = element

    def attack(self):
        print(f'Attacking with {self.element}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'{self.name} is beginning their attack, be prepared!')
        arrows_left = 0
        attack_num = int(input('Enter amount of arrows you want to shoot: '))
        if attack_num <= self.arrows:
            arrow_left = self.arrows - attack_num
            print(f'Attacking with {attack_num} arrows, you now have {arrow_left} arrows left ')
        else:
            print(f"I'm sorry {self.name}, you don't have enough arrows to make this attack. Currently you only hold {self.arrows}")


# Instantiated objects
wizard1 = Wizard('Dr. Strange', 'Fire', 'DrStrange@gmail.com')

archer1 = Archer('Green Arrow', 100)

print(wizard1.email)
# archer1.attack()
print(isinstance(wizard1, object))
