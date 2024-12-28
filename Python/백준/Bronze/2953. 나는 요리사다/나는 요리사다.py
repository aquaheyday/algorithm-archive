import sys
input = sys.stdin.readline

a = []
for _ in range(5):
    x = list(map(int, input().split()))
    a.append(sum(x))
     
print(a.index(max(a)) + 1, max(a))