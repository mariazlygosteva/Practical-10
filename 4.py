chess = input()
letter = chess[0]
number = chess[1:]
letters = 'abcdefgh'

if letters.index(letter.lower()) % 2 == 0:
    print('Белый' if int(number) % 2 == 0 else 'Черный')
else:
    print('Черный' if int(number) % 2 == 0 else 'Белый')