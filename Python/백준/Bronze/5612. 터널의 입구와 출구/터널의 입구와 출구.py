import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

res = m

for i in range(n):
    a,b = map(int, input().split())
    
    m = m + a - b
    
    if m < 0:
        res = 0
        break
    elif res < m:
        res = m
print(res)