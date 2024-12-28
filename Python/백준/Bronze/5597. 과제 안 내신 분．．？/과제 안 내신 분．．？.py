import sys
input = sys.stdin.readline

a = list(range(1, 31))
s = set(a)

for i in range(28):
    n = int(input())
    s.remove(n)

b = list(s)
b.sort()

print(*b, sep='\n')