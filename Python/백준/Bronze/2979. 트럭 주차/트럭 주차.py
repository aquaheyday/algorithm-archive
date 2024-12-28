import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
res = 0
x = [0] * 101

for i in range(3):
    a, b = map(int, input().split())
    for y in range(a, b):
        x[y] += 1

for i in x:
    if i == 1:
        res += A
    elif i == 2:
        res += B * 2
    elif i == 3:
        res += C * 3
        
print(res)