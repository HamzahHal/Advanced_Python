class Toy():
    def __init__(self, colour, age):
        self.colour = colour
        self.age = age
        self.my_dict = {
            'name': 'ytppt',
            'has pets': False

        }

    def __str__(self):
        return f'{self.colour}'

    def __len__(self):
        return 5

    def __call__(self):
        print('yesssss')

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('Red', 35)
print(action_figure.__str__())
print(len(action_figure))
print(action_figure())
print(action_figure['name'])
