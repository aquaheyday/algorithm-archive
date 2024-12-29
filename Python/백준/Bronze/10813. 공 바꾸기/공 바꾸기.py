import sys
input = sys.stdin.readline

n, m = map(int, input().split())
res = [0] * n
for i in range(n):
    res[i] = i + 1
    
for i in range(m):
    a, b = map(int, input().split())
    
    t = res[b - 1]
    res[b - 1] = res[a - 1]
    res[a - 1] = t
    
print(*res)