import sys
input = sys.stdin.readline

n = int(input())
res = 0
for i in range(n):
    c, a = map(int, input().split())
    
    res += a % c
    
print(res)