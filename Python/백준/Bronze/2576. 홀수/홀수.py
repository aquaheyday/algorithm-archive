import sys
input = sys.stdin.readline

m = 100
res = 0

for i in range(7):
    n = int(input())
    
    if n % 2 == 1:
        res += n
        m = min(m, n)
if res == 0:
    print(-1)
else:
    print(res)
    print(m)