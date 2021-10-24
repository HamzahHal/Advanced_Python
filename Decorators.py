# Higher Order Function (HOC)
def Hello(func):
    return func()


def greet():
    print("still here")


a = Hello(greet)
print(a)
