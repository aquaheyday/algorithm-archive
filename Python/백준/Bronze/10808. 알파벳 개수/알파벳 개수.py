import sys
input = sys.stdin.readline

a = input().rstrip()
b = [0] * 26

for x in a:
    b[ord(x) - ord('a')] += 1
    
print(*b)