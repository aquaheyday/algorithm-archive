import sys
input = sys.stdin.readline

n = int(input())
res = 0

while n > 0:
    i = 1
    while n >= i:
        n -= i
        i += 1
        res += 1
        
print(res)
        
    