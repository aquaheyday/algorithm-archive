n, k = map(int, input().split())
r = []

for i in range(1, n + 1):
    if n % i == 0:
        r.append(i)
        
if len(r) >= k:
    print(r[k - 1])
else:
    print(0)