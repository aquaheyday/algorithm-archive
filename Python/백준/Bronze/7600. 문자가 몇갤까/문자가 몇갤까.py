import sys
input = sys.stdin.readline

while True:
    a = input().rstrip()
    
    if a == '#':
        break
    
    s = set()
    
    for x in a:
        if x.isalpha():
            s.add(x.lower())
    print(len(s))