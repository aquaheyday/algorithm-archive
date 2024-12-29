import sys
input = sys.stdin.readline

a,b = map(int, input().split())
x,y = map(int, input().split())

playerA = b
playerB = y

while True:
    playerA -= x
    playerB -= a
    
    if playerA > 0 and playerB <= 0:
        print('PLAYER A')
        break
    elif playerA <= 0 and playerB > 0:
        print('PLAYER B')
        break
    elif playerA <= 0 and playerB <= 0:
        print('DRAW')
        break
        
      
    
    