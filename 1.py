import math

radius = 6.5
length, width = map(int, input().split('x'))
diagonal = math.sqrt(length ** 2 + width ** 2)

if diagonal <= 2 * radius:
    print('Да')
else:
    print('Нет')