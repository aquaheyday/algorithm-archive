import sys
input = sys.stdin.readline

N, M = map(int, input().split())
res = [0] * (N + 1)

for t in range(M):
    i, j, k = map(int, input().split())
    
    for x in range(i, j + 1):
        res[x] = k
        
print(*res[1:])
    