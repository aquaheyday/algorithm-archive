import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

x = sum([a,b,c,d]) - min([a,b,c,d])
y = max([e,f])

print(sum([x,y]))