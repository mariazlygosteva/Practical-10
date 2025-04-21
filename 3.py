N, M = map(int, input().split('x'))
K = int(input())

if K <= N * M and (K % N == 0 or K % M == 0):
        print('Успешно')
else:
        print('Неосуществимо')