import sys
input = sys.stdin.readline

a,b = map(int, input().split())

p = [1] * (b + 1)
p[1] = 0
y = int(b ** 0.5)

for i in range(2, y + 1):
    if p[i] == 1:
        for j in range(i + i, b + 1, i):
            p[j] = 0
            
for i in range(a, b + 1):
    if p[i] == 1:
        print(i)