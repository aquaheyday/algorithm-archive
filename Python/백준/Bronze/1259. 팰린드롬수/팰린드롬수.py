import sys
input = sys.stdin.readline

while True:
    a = input().rstrip()
    if a == '0':
        break
        
    if a[::-1] == a:
        print('yes')
    else:
        print('no')
    