import sys

N = int(sys.stdin.readline().strip())

d = len(str(N))
start = max(1, N - 9 * d)

def digit_sum(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

answer = 0
for m in range(start, N):
    if m + digit_sum(m) == N:
        answer = m
        break

print(answer)
