import sys
input = sys.stdin.readline
res = 0
n = int(input())

while True:
    res += 1
    if n == 1:
        break
        
    
    if n % 2 == 0:
        n /= 2
    else:
        n = 3 * n + 1
        
print(res)