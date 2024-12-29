import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

res = 0

if a < 0:
    res += abs(a) * c
    res += d
    res += b * e
elif a == 0:
    res += d
else:
    res += (b - a) * e
    
print(res)