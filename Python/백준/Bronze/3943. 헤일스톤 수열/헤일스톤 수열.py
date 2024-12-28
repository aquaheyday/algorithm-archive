import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    t = int(input())
    res = t
    
    while True:
        if t == 1:
            break
        if t % 2 == 0:
            t //= 2
        else:
            t = t * 3 + 1
            if t > res:
                res = t
    print(res)
        
    
    