import sys
import collections
input = sys.stdin.readline

n = int(input())
s = collections.deque()

for i in range(n):
    a = int(input())
    
    if a == 0:
        s.pop()
    else:
        s.append(a)
        
print(sum(s))
    