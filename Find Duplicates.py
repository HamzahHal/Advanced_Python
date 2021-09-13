# Exercise: Check for duplicates in list:
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
dupes = []

for char in some_list:
    if some_list.count(char) > 1:
        if char not in dupes:
            dupes.append(char)

print(dupes)