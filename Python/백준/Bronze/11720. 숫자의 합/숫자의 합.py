import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, list(input().rstrip())))

print(sum(a))