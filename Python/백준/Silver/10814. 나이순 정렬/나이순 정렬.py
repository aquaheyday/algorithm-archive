import sys
input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    x, y = input().split()
    a.append([int(x),i, y])
    
a.sort()

for x,i,y in a:
    print(x,y)
    