import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x = list(map(int, input().split()))
res = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if res < x[i] + x[j] + x[k] <= m:
                res = x[i] + x[j] + x[k]
print(res)
                