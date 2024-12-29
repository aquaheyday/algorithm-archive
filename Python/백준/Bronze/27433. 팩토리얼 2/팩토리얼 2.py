import sys
input = sys.stdin.readline

def f(x):
    if x == 0:
        return 1
    else:
        return x * f(x - 1)
       
n = int(input())
res = f(n)
    

print(res)