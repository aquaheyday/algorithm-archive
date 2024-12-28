import sys
input = sys.stdin.readline

n = int(input())
t = [];

for i in range(n):
    a = int(input())
    t.append(a)
    
t.sort()
print(*t, sep = '\n')