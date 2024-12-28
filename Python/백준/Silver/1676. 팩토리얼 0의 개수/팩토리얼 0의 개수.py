import sys
input = sys.stdin.readline

n = int(input())

r = n // 5 + (n // (5 ** 2)) + (n // (5 ** 3))

print(r)