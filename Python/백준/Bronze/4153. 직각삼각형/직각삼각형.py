import sys
input = sys.stdin.readline

while True:
    a,b,c = map(int, input().split())
    
    if a == b == c == 0:
        break
    
    if a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b:
        print('right')
    else:
        print('wrong')
    

