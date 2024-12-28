import sys
input = sys.stdin.readline

a = 100
b = 100

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    
    if x > y:
        b -= x
    elif y > x:
        a -= y

print(a)
print(b)