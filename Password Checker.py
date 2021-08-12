# Username = input("Enter username: ")
# Password = input("Enter Password: ")

# print(f'password is {len(Password)} and username is {len(Username)} letters long')
# print(f'Your password is {hidden_password} and your username is "{Username}"')


Card_Number = '543579349573495'

hidden_number = '*' * (len(Card_Number) - len(Card_Number[10:])) + Card_Number[10:]

print(len(Card_Number))
print(len(hidden_number))
print(hidden_number)
