import sys
input = sys.stdin.readline

n = int(input())
r = -1

for i in range(5):
    now = n - 3 * i
    
    if now >= 0 and now % 5 == 0:
        r = i + now // 5
        break
print(r)