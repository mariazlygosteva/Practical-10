position = int(input())
sequence = ''
sequence += '0'

for number in range(1, 201):
        sequence += str(number)
print(sequence[position - 1])