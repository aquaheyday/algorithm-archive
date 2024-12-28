import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    x = n - i
    print(' ' * i + '*' * (x * 2 - 1))