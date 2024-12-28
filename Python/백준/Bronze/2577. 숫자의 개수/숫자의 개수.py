import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

t = a * b * c
r = [0] * 10

for x in str(t):
    r[int(x)] += 1
    
print(*r, sep = '\n')
