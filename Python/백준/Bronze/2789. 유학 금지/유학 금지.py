import sys
input = sys.stdin.readline

s = input().rstrip()
text = 'CAMBRIDGE'
for i in text:
    s = s.replace(i, '')
print(s)