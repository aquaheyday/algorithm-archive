import sys
input = sys.stdin.readline

val = 0
idx = 0

for i in range(9):
    x = int(input())
    if val < x:
        val = x
        idx = i + 1

        
print(val)
print(idx)