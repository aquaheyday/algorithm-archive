import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c = int(input())

x = (a + b) -  (c * 2)

if x >= 0:
    print(x)
else:
    print(a + b)