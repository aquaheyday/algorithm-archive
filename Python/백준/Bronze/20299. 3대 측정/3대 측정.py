import sys
input = sys.stdin.readline

n, k, l = map(int, input().split())
res = []

for i in range(n):
    a = list(map(int, input().split()))
    
    if l <= min(a) and k <= sum(a):
        res.extend(a)

print(len(res) // 3)
print(*res)