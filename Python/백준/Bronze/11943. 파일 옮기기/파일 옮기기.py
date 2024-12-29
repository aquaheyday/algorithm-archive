import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())

x = b + c
y = a + d

if x <= y:
    print(x)
else:
    print(y)