import sys
input = sys.stdin.readline

N, m, M, T, R = map(int, input().split())

current_heart_rate = m
exercise_time = 0
time = 0

if m + T > M:
    print(-1)
    sys.exit()

while exercise_time < N:
    if current_heart_rate + T <= M:
        current_heart_rate += T
        exercise_time += 1
    else:
        current_heart_rate = max(current_heart_rate - R, m)
    
    time += 1


print(time)
