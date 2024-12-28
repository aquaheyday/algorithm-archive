import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split())) + [300000001]
i, j = 0, 0
now = a[0]
res = 0

while j < n:
    if now == m:
        res += 1
        now -= a[i]
        i += 1
        j += 1
        now += a[j]
    elif now < m:
        j += 1
        now += a[j]
    else:
        now -= a[i]
        i += 1
        
print(res)

