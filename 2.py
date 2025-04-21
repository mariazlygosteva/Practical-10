A, B = map(int, input().split('x'))
C, D, E = map(int, input().split('x'))

if ((A >= C and B >= D) or (A >= D and B >= C) or (A >= C and B >= E) or (
        A >= E and B >= C) or (A >= D and B >= E) or (A >= E and B >= D)):
    print('Да')
else:
    print('Нет')