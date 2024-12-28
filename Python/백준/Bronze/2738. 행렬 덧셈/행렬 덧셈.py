import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
b = [list(map(int, input().split())) for i in range(n)]
res = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        res[i][j] = a[i][j] + b[i][j]
        
for x in res:
    print(*x)
