import sys
import math
input = sys.stdin.readline

N = int(input())
trees = [int(input()) for _ in range(N)]

diffs = [trees[i+1] - trees[i] for i in range(N-1)]

g = diffs[0]
for d in diffs[1:]:
    g = math.gcd(g, d)

result = sum((d // g) - 1 for d in diffs)

print(result)
