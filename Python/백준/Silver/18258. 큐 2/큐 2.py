import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

q = deque()
output = []

for _ in range(N):
    cmd = input().split()

    if cmd[0] == 'push':
        q.append(cmd[1])

    elif cmd[0] == 'pop':
        if q:
            output.append(q.popleft())
        else:
            output.append('-1')

    elif cmd[0] == 'size':
        output.append(str(len(q)))

    elif cmd[0] == 'empty':
        output.append('0' if q else '1')

    elif cmd[0] == 'front':
        if q:
            output.append(q[0])
        else:
            output.append('-1')

    elif cmd[0] == 'back':
        if q:
            output.append(q[-1])
        else:
            output.append('-1')

print("\n".join(output))
