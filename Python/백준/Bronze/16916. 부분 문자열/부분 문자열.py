import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
if b in a:
    print(1)
else:
    print(0)