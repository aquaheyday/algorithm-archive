import sys
input = sys.stdin.readline

a = input().rstrip() + 'ILOVEYONSEI'
res = 0

for i in range(1, len(a)):
    x = ord(a[i -1])
    y = ord(a[i])
    res += abs(x - y)
    
print(res)
