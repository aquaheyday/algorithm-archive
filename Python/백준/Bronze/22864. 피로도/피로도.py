import sys
input = sys.stdin.readline


A, B, C, M = map(int, input().split())
res = 0
p = 0

for i in range(24):
    if p + A > M:
        p -= C
        if p < 0:
            p = 0
    else:
        res += B
        p += A
        
print(res)