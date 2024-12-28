import sys
input = sys.stdin.readline

n = int(input())

for x in range(n):
    a = input().split()
    res = []
    for y in a:
        res.append(y[::-1])
        
    print(*res)