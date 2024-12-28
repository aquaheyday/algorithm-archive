import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    res = 0
    p = int(input())
    m = int(input())
    
    res += p
    
    for i in range(m):
        q, p = map(int, input().split())
        
        res += q * p
        
    print(res)