import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
res = [list(map(int, input().split())) for i in range(n)]
c = 0

for i in range(n):
    if res[a - 1][i] > res[a - 1][b - 1]:
        c = 1
    elif res[i][b - 1] > res[a - 1][b - 1]:
        c = 1
        
if c == 1:
    print('ANGRY')
else:
    print('HAPPY')