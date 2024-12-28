import sys
input = sys.stdin.readline

a = input().rstrip()
x = []

for i in a:
    x.append(int(i))
    
x.sort(reverse = True)

print(*x, sep = '')