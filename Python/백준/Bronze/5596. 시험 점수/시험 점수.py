import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
b = list(map(int, input().split()))

x = sum(a)
y = sum(b)

print(max(x, y))