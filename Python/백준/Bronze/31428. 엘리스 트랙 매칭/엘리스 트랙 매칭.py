import sys
input = sys.stdin.readline

n = int(input())
a = input().split()
d = {'C': 0, 'S': 0, 'I': 0, 'A': 0}
b = input().rstrip()

for x in a:
    d[x] += 1
    
print(d[b])
    