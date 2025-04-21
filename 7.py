K = int(input())
possible = False

for x in range(K // 5 + 1):
    remaining = K - 5 * x
    if remaining >= 0 and remaining % 7 == 0:
        possible = True
        break

if possible:
    print('Да')
else:
    print('Нет')
