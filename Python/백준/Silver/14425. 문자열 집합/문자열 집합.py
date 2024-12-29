import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set()
res = 0

for i in range(n):
    x = input().rstrip()
    a.add(x)
    
for i in range(m):
    x = input().rstrip()
    
    if x in a:
        res += 1
        
print(res)
        