import sys
input = sys.stdin.readline

n = int(input())
r = [0] * 101
a = list(map(int, input().split()))
cnt = 0

for i in a:
    if (r[i] > 0):
        cnt += 1
    else:
        r[i] += 1
        
print(cnt)
