import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = [0]

for x in a:
    b.append(b[-1] + x)

for k in range(m):
    i, j = map(int, input().split())
    print(b[j] - b[i - 1])