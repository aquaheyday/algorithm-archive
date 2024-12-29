import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    a = input().rstrip()
    res = 0
    
    for j, v in enumerate(a):
        
        if j % 2 == 1:
            x = int(v)
        else:
            x = int(v) * 2
            
            if x >= 10:
                x = x // 10 + x % 10
                
        res += x
        
    if res % 10 == 0:
        print('T')
    else:
        print('F')
            
       
            
        