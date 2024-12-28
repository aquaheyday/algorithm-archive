import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
res = 0

for x in a:
    res += x * x
    
print(res % 10)