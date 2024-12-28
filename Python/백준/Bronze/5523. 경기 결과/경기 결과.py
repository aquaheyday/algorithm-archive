import sys
input = sys.stdin.readline

n = int(input())

x = 0
y = 0

for i in range(n):
    a,b = map(int, input().split())
    
    if a > b:
        x += 1
    elif b > a:
        y += 1
        
print(x, y)
    