import sys
input = sys.stdin.readline

for i in range(3):
    a = list(map(int, input().split()))
    x = sum(a)
    
    if x == 3:
        print('A')
    elif x == 2:
        print('B')
    elif x == 1:
        print('C')
    elif x == 0:
        print('D')
    else:
        print('E')
             
            
    
    
    