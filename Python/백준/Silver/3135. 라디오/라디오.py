import sys
input = sys.stdin.readline

a,b = map(int, input().split())
n = int(input())

r = []
r.append(abs(a - b))

for i in range(n):
    x = int(input())
    
    r.append(abs(x - b)  + 1)
    
print(min(r))    