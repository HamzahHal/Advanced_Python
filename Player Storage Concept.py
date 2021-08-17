# Game data storage using a dictionary inside a list
Player_Data = [
    {
        'Player Name': 'K1LL3R101',
        'Age': 2500,
        'Base Health': 100,
        'Additional Health': 0,
        'Items Equippable': 5,
        'Items Equipped': ['Sword', 'Gun', 'Spear']
    },
    {
        'Player Name': 'TaleOfScripting',
        'Age': 53443,
        'Base Health': 100,
        'Additional Health': 433,
        'Items Equippable': 58,
        'Items Equipped': 34,
    }
]

print(Player_Data[0]['Player Name'])

Player_Data[0]['Player Name'] = 'VetexGames'
Player_Data[1]['Player Name'] = 'ShadeOfAzure'


print(Player_Data[0]['Items Equipped'])
print(Player_Data[1]['Player Name'])
print(Player_Data[1]['Age'])

Item_len = len(Player_Data[0]['Items Equipped'])
print(Item_len)

slots_left = Player_Data[0]['Items Equippable'] - Item_len
print(slots_left)

if Item_len < Player_Data[0]['Items Equippable']:
    print(f'You have {slots_left} equip slots left')