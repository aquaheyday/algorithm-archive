import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
m.sort()

r = 0

for i in m:
    r += i / m[n - 1] * 100
    
print(r / n)