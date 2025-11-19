import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dq = deque()
out = []   # 출력 성능 최적화 위해 리스트에 모아두기

for _ in range(n):
    cmd = input().split()

    if cmd[0] == '1':
        dq.appendleft(int(cmd[1]))
    elif cmd[0] == '2':
        dq.append(int(cmd[1]))
    elif cmd[0] == '3':
        if dq:
            out.append(str(dq.popleft()))
        else:
            out.append('-1')
    elif cmd[0] == '4':
        if dq:
            out.append(str(dq.pop()))
        else:
            out.append('-1')
    elif cmd[0] == '5':
        out.append(str(len(dq)))
    elif cmd[0] == '6':
        out.append('0' if dq else '1')
    elif cmd[0] == '7':
        if dq:
            out.append(str(dq[0]))
        else:
            out.append('-1')
    elif cmd[0] == '8':
        if dq:
            out.append(str(dq[-1]))
        else:
            out.append('-1')

print("\n".join(out))
