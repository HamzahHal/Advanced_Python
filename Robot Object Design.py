class RobotCharacter:

    def __init__(self, power=0, velocity=0, weight=0):
        self.power = power
        self.velocity = velocity
        self.weight = weight

    def new_movement(self):
        if self.power > 40:
            return self.velocity
        else:
            self.velocity -= 3
            return self.velocity


robot1 = RobotCharacter(20, 10, 300)

print(robot1.new_movement())
print(type(robot1.new_movement()))

