# # Scope - what variables do i have access to?
# # if True:
# #     x = 10
# # def some_fun():
# #     total = 100
# #     print(total)
# #
# # print(x)
#
# a = 1
#
#
# def parent():
#     def confusion():
#         return a
#
#     return confusion()
#
#
# print(parent())
# print(a)
#
#
# def confusion():
#     return a
#
#
# def confusion_new(b):
#     a = 90
#
#
# confusion_new(500)

total = 0


def count(total):
    total += 1
    return total


print(count(count(count(total))))


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal".replace
        print('inner: ', x)
    inner()
    print('outer: ', x)


outer()

# 1 - start with local
# 2 - Parent local
# 3 - Global
# 4 - built in python functions
