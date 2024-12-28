import sys
input = sys.stdin.readline

a, b = input().split()
na, nb = len(a), len(b)
res = 50

for i in range(nb - na + 1):
    cnt = 0
    
    for j in range(na):
        if a[j] != b[i + j]:
            cnt += 1
            
    res = min(res, cnt)
print(res)      