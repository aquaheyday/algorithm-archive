import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
b = sorted(a)

if a == b:
    print('Good')
else:
    print('Bad')