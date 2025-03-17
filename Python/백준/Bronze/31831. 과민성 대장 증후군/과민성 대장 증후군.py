import sys
input = sys.stdin.readline

n,m = map(int, input().split())
a = list(map(int, input().split()))
res = 0
cnt = 0

for i in a:

    res += i
    
    if res < 0:
        res = 0
    if res >= m:
        cnt += 1
        
print(cnt)