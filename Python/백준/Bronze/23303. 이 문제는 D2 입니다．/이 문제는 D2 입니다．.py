import sys
input = sys.stdin.readline

a = input().rstrip()

if 'd2' in a or 'D2' in a:
    print('D2')
else:
    print('unrated')