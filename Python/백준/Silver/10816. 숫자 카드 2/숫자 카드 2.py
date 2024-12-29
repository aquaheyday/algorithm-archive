import sys
import collections
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
d = collections.defaultdict(int)

for x in a:
    d[x] += 1

m = int(input())
b = list(map(int, input().split()))
res = []

for x in b:
    res.append(d[x])
    
print(*res)
    
