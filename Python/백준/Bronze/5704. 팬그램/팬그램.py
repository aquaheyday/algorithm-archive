import sys
input = sys.stdin.readline

while True:
    a = input().rstrip()

    if a == '*':
        break
        
    b = set()
    
    for x in a:
        if x.islower():
            b.add(x)
            
    if len(b) == 26:
        print('Y')
    else:
        print('N')
        