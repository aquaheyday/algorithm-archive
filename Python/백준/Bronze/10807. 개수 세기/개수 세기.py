import sys
input = sys.stdin.readline

n = int(input())
t = tuple(map(int, input().split()))
v = int(input())

print(t.count(v))