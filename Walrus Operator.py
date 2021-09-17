a = 'Helloooooooooooooo'

if (n := len(a)) > 10:
    print(f"too long {n} elements")

num1 = '3020000000000'

while i := len(num1) < 10:
    print('shit is long')
else:
    print('shit dont exist')


while (n := len(a)) > 1:
    print(n)
    a = a[:-1]
    
    
print(a)