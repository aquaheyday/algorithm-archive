import sys
input = sys.stdin.readline

n,m = map(int, input().split())
x = abs(n - m)

print(x)