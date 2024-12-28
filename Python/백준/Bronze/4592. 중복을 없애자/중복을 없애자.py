import sys
input = sys.stdin.readline

while True:
    n, *a = list(map(int, input().split()))
    res = []
    if (n == 0):
        break
        
    res.append(a[0])
    
    for x in a[1:]:
        if res[-1] == x:
            continue
        res.append(x)
        
    print(*res, '$')
            
        
        