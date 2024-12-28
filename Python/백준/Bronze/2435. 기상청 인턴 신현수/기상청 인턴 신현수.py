import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [0]

for x in a:
    b.append(b[-1] + x)
    
res = -100 * k

for i in range(k, n + 1):
    res = max(res, b[i] - b[i - k])
    
print(res)
