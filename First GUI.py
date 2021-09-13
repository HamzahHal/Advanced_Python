# Exercise!
# Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
# Attempted Exercise
i = ' '
k = '*'
image = []

for index, integer in enumerate(picture):
    if integer == 0:
        space = ' '
        image[index] += space
    elif integer == 1:
        star = '*'
        image[index] += star
    print(image)

# for num in picture:
#     if num == 0:
#         image.append(i)
#     elif num == 1:
#         image.append(k)
#         continue
print(image)

# Solution
for row in picture:
    for pixel in row:
        if pixel == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print('')