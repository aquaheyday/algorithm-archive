import sys
input = sys.stdin.readline

a = input().rstrip()
res = ''

for x in a:
    if x.islower():
        res += x.upper()
    else:
        res += x.lower()
        
print(res)
        