import sys
input = sys.stdin.readline

n = int(input())

for x in range(1, 10):
    print(n, '*', x, '=', n * x)