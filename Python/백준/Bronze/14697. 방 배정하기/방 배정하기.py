import sys
input = sys.stdin.readline

a, b, c, n = map(int, input().split())
res = 0

for i in range(n // a + 1):
    for j in range(n // b + 1):
        for k in range(n // c + 1):
            if a * i + b * j + c * k == n:
                res = 1
                break
    
print(res)