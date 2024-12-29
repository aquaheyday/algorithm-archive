import sys
import heapq
input = sys.stdin.readline

n = int(input())
h = []

for i in range(n):
    a = list(map(int, input().split()))
    
    if a[0] == 0:
        if len(h) == 0:
            print(-1)
        else:
            print(-h[0])
            heapq.heappop(h)
    else:
        for x in a[1:]:
            heapq.heappush(h, -x)