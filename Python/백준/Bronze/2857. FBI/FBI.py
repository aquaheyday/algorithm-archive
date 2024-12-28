import sys
input = sys.stdin.readline

x = []

for i in range(5):
    a = input().rstrip();
    
    if 'FBI' in a:
        x.append(i + 1)

if len(x) > 0:
    print(*x)
else:
    print('HE GOT AWAY!')
        