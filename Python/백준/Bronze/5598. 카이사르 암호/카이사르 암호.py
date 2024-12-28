import sys
input = sys.stdin.readline

a = input().rstrip()
res = ''

for x in a:
    c = ord(x) - 3
    
    if c < ord('A'):
        c += 26
    
    res += chr(c)

print(res)