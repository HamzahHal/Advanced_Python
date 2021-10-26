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
    def wrap_func(*args, **kwargs):
        print("******")
        func(*args, **kwargs)
        print("******")

    return wrap_func


@my_decorator
def hey(greetings, emoji=":)"):
    print(greetings, emoji)


# @my_decorator
# def bye():
#     print("Bye")


hey("hi bitches")
# bye()
