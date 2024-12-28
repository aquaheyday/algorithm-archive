import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set()
b = set()
for i in range(n):
    x = input().rstrip()
    b.add(x)
    
for i in range(m):
    x = input().rstrip()
    a.add(x)
    
s = a & b 
s = list(s)
s.sort()

print(len(s))
print(*s, sep = '\n')