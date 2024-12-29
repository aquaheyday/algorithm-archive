import sys
input = sys.stdin.readline

n = int(input())
y = 0

for i in range(n):
    x = int(input())
    y += x

if n % 2 == 0:
    t = n // 2
else:
    t = n // 2 + 1
    
if t <= y:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')
    