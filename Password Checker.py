Username = input("Enter username: ")
Password = input("Enter Password: ")

hidden_password = '*' * len(Password)

print(f'password is {len(Password)} and usename is {len(Username)} letters long')
print(f'Your password is {hidden_password} and your username is "{Username}"')