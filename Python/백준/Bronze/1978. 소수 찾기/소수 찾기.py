import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
r = 0

for i in a:
    if i == 1:
        continue
        
    f = 0
    for j in range(2, i - 1):
        if i % j == 0:
            f = 1
            break
    if f == 0:
        r += 1
print(r)