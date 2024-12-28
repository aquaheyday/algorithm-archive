import sys
import heapq
input = sys.stdin.readline

n = int(input())
a = int(input())
h = []

for i in range(n - 1):
    x = int(input())
    heapq.heappush(h, -x)
    
res = 0

if n > 1:
    while True:
        x = -heapq.heappop(h)
        
        if a > x:
            break
        res += 1
        x -= 1
        a += 1
        heapq.heappush(h, -x)
        
print(res)