import sys
input = sys.stdin.readline

n = int(input())
x = []

for i in range(n):
    a,b,c,d = input().split()
    x.append([-int(b),int(c),-int(d),a])

x.sort()
    
for b,c,d,a in x:
    print(a)
