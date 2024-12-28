import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

p = [1] * (m + 1)
p[1] = 0
y = int(m ** 0.5)

for i in range(2, y + 1):
    if p[i] == 1:
        for j in range(i + i, m + 1, i):
            p[j] = 0

r = []

for i in range(n, m + 1):
    if p[i] == 1:
        r.append(i)

if len(r) > 0:
    print(sum(r))
    print(r[0])
else:
    print(-1)