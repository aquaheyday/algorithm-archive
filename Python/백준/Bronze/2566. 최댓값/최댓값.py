import sys
input = sys.stdin.readline

max = 0
idx = [0, 0]

for i in range(9):
    a = list(map(int, input().split()))
    
    for j in range(9):
        if max <= a[j]:
            max = a[j]
            idx = [i + 1, j + 1]
print(max)
print(idx[0], idx[1])