import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(range(1, n + 1))

for i in range(n - 1):
    q.popleft()
    a = q.popleft()
    q.append(a)

print(q[0])