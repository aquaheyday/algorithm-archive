import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    t = n - i
    print(' ' * i + '*' * t)