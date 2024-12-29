import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def f(n):
    if n == 0:
        return 1
    else:
        return n * f(n - 1)

n = int(input())
res = f(n)

print(res)