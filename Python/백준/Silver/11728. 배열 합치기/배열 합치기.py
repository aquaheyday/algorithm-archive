import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = []
i, j = 0, 0

while i < n and j < m:
    if a[i] < b [j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1
        
if i == n:
    while j <  m:
        res.append(b[j])
        j +=1
else:
    while i < n:
        res.append(a[i])
        i += 1
print(*res)
    
        
        
        
        
    