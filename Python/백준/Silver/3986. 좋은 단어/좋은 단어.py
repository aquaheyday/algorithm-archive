import sys
import collections
input = sys.stdin.readline

n = int(input())
r = 0

for _ in range(n):
    text = input().strip()
    f = collections.deque()
    
    for s in text:
        if not len(f):
            f.append(s)
        elif f[-1] == s:
            f.pop()
        else:
            f.append(s)
    
    if not len(f):
        r += 1

print(r)
