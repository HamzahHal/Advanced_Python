# messy clean code
def is_even(num):
    if num % 2:
        return False
    else:
        return True

print(is_even(51))
print(is_even(22))

# clean code
def is_even(num):
    return num % 2 == 0;

print(is_even(51))
print(is_even(22))



