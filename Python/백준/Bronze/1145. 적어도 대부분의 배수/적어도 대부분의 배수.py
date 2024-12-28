import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
res = 0

for i in range(1, 10000000):
    cnt = 0
    
    for x in a:
        if i % x == 0:
            cnt += 1
    if cnt >= 3:
        res = i
        break
    
print(res)