import sys
input = sys.stdin.readline

n = int(input())
a = []

for x in range(n):
    b = list(map(int, input().split()))
    v = 0
    
    for i in range(5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                w = (b[i] + b[j] + b[k]) % 10
                v = max(v, w)
                
    a.append([v, x + 1])
    
a.sort()

print(a[-1][1])