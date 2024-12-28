import sys
input = sys.stdin.readline

    
res = 0
    
for n in range(1, 9):
    if n % 2 == 0:
        c = 0
    else:
        c = 1
    
    a = input().rstrip()
    
    for x in a:
        if c == 0:
            c = 1
        else:
            c = 0
            if x == 'F':
                res += 1
            
print(res)
                
