import sys
input = sys.stdin.readline

n = int(input())
f = int(input())

n //= 100
n *= 100
res = 0

for i in range(100):
    if (n + i) % f == 0:
        res = i
        break

print(f'{res:02d}')


