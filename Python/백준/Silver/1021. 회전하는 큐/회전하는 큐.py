import sys
import collections
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
q = collections.deque(range(1, n + 1))
res = 0

for x in a:
    q1 = q.copy()
    cnt1 = 0
    
    while q1[0] != x:
        b = q1.popleft()
        q1.append(b)
        cnt1 += 1
        
    q2 = q.copy()
    cnt2 = 0
    
    while q2[0] != x:
        b = q2.pop()
        q2.appendleft(b)
        cnt2 += 1
        
    res += min(cnt1, cnt2)
    q = q1.copy()
    q.popleft()
    
print(res)
