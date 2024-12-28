import sys
input = sys.stdin.readline

while True:
    a,b,c = map(int, input().split())
    if a == b == c == 0:
        break
    
    if a + b <= c or a + c <= b or b + c <= a:
        print('Invalid')
    elif a == b == c:
        print('Equilateral')
    elif a == c != b or a == b != c or b == c != a:
        print('Isosceles')
    elif a != b != c:
        print('Scalene')