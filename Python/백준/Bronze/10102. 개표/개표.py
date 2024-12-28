import sys
input = sys.stdin.readline

n = int(input())
text = input().rstrip()

a = text.count('A')
b = text.count('B')
if a > b:
    print('A')
elif b > a:
    print('B')
else:
    print('Tie')

    