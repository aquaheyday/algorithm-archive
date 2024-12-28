import sys
input = sys.stdin.readline

k, n, m = map(int, input().split())

x = k * n
if x > m:
    print(x - m)
else:
    print(0)