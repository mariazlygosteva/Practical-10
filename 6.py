N, K, M = map(int, input().split(' '))
total_rides = N * 2
num = round(total_rides / K)
total_time = num * M
print(total_time)