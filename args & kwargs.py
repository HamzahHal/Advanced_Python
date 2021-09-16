# *args **kwargs

def super_fun(name,*args, i='hi', **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_fun('hamzah',1,2,3,4,5, num1=5, num2=10))

def multiply_add(*args,**kwargs):
    total = 0
    for x in kwargs.values():
        total += x
    return sum(args) * total

print(multiply_add(9,1,num=1,n2=1,n3=1))


# Rule: params, *args, default params, **kwargs