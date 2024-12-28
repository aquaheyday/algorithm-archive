import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    a = input().rstrip()
    res = 0
    sum = 1

    for x in a:
        if x == 'O':
            res += sum
            sum += 1
        else:
            sum = 1

    print(res)
        