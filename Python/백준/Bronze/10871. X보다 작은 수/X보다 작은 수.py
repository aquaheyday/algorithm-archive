import sys
input = sys.stdin.readline

n, x = map(int, input().split())
t = list(map(int, input().split()))

for i in t:
    if i < x:
        print(i)
    