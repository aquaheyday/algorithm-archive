import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    p = int(input())
    a = []
    
    for j in range(p):
        c, x = input().split()
        a.append([int(c), x])
    a.sort()
    
    print(a[-1][1])
    