import sys
input = sys.stdin.readline

n = int(input())
a = []
res = [1] * n

for i in range(n):
    x, y = map(int, input().split())
    
    a.append([x, y])
    
for i in range(n):
    x1, y1 = a[i]
    for j in range(i + 1, n):
        x2, y2 = a[j]
        
        if x1 > x2 and y1 > y2:
            res[j] += 1
        elif x1 < x2 and y1 < y2:
            res[i] += 1
print(*res)
            
        
    
    
    