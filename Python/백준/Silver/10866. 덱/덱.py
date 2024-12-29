import sys
import collections
input = sys.stdin.readline

n = int(input())
d = collections.deque()

for i in range(n):
    a = input().rstrip()
    
    if a == 'pop_front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
            d.popleft()
    elif a == 'pop_back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
            d.pop()
    elif a == 'size':
        print(len(d))
    elif a == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif a == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif a == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
    else:
        a, x = a.split()
        x = int(x)
        if a == 'push_front':
            d.appendleft(x)
        else:
            d.append(x)