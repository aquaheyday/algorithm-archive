import sys
input = sys.stdin.readline

while True:
    a,b,c = map(int, input().split())
    
    if a == b == c == 0:
        break
        
    x = b - a
    if a == 0:
        y = 0
    else:
        y = b / a
    
    if (b + x) == c:
        print('AP', c + x)
    elif (b * y) == c:
        print('GP', int(c * y))