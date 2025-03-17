import sys
input = sys.stdin.readline

n = int(input())
res = 0

for i in range(n):
    a,b,c,d,e,f,g = map(int, input().split())
    x = max(a,b)
    y = [c,d,e,f,g]
    y.sort()
    
    v = x + y[3] + y[4]
    res = max(res, v)
    
print(res)