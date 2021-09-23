# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
Cat1 = Cat('Tom', 30)
Cat2 = Cat('Jerry', 32)
Cat3 = Cat('Callum', 2230)


# 2 Create a function that finds the oldest cat
def findOldest():
    oldest = 0
    my_list = [Cat1.age, Cat2.age, Cat3.age]
    for i in my_list:
        if i > oldest:
            oldest = i
            # See the process
            print(oldest)
    return oldest


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is the {findOldest()}.')
