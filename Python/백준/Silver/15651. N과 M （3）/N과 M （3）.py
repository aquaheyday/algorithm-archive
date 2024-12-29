import sys
import itertools
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(range(1, n + 1))

for x in itertools.product(a, repeat = m):
    print(*x)