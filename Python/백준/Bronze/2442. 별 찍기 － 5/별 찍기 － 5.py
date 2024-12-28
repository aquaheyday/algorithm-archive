import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    t = i + 1
    print(' ' * (n - t) + '*' * (t * 2 - 1))