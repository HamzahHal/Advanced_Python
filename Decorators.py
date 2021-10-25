# Higher Order Function (HOC)
def Hello(func):
    return func()


def greet():
    print("still here")


a = Hello(greet)
print(a)


def tester(func):
    func()


def tester2():
    def func():
        return 5

    return func


# Decorator
def my_decorator(func):
    def wrap_func():
        print("******")
        func()
        design = input("Enter design sign: ")
        key = len(design * 4)
        print(design * key)

    return wrap_func


@my_decorator
def hey():
    print("Hey")


@my_decorator
def bye():
    print("Bye")


hey()
bye()
