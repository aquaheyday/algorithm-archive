import sys
input = sys.stdin.readline

a = []
s = 0
res = []

for i in range(9):
    x = int(input())
    a.append(x)
    s += x

for i in range(9):
    for j in range(9):
        if s - a[i] - a[j] == 100:
            res = (a[i], a[j])

for i in range(9):
    if a[i] not in res:
        print(a[i])
