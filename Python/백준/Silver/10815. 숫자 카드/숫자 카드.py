import sys
input = sys.stdin.readline

n = int(input())
a = set(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

res = []

for x in b:
    if x in a:
        res.append(1)
    else:
        res.append(0)
        
print(*res)
    