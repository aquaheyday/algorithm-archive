import sys
input = sys.stdin.readline

n = int(input())
s = {
    'Never gonna give you up',
    'Never gonna let you down',
    'Never gonna run around and desert you',
    'Never gonna make you cry',
    'Never gonna say goodbye',
    'Never gonna tell a lie and hurt you',
    'Never gonna stop'
}
cnt = 0

for i in range(n):
    a = input().rstrip()
    
    if a in s:
        cnt += 1
        
if n == cnt:
    print('No')
else:
    print('Yes')
    