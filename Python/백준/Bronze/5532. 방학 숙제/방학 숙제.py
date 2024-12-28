import sys
input = sys.stdin.readline

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A % C > 0:
    x = 1
else:
    x = 0
    
if B % D > 0:
    v = 1
else:
    v = 0
    
y = L - (A // C + x)
z = L - (B // D + v)

if y > z:
    print(z)
else:
    print(y)


