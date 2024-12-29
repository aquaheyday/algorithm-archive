import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

now = sum(a[:m])
res = now

for i in range(m, n):
    now += a[i]
    now -= a[i - m]
    res = max(res, now)
    
print(res)