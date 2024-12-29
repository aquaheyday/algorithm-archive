import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
q = deque(range(1, n + 1))
res = []

for i in range(n):
    for j in range(k - 1):
        a = q.popleft()
        q.append(a)
    a = q.popleft()
    res.append(a)
print('<', end = '')
print(*res, sep = ', ', end = '')
print('>', end = '')