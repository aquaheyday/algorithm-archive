import sys
input = sys.stdin.readline

n = int(input())
s = set()

for i in range(n):
    a = input().rstrip()
    s.add((len(a), a))
    
s = list(s)
s.sort()

for x, y in s:
    print(y)
    