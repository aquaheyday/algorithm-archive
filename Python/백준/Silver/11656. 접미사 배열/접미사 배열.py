import sys
input = sys.stdin.readline

s = input().rstrip()
n = len(s)
a = []

for i in range(n):
    a.append(s[i:])
    
a.sort()

print(*a, sep='\n')
    
