import sys
input = sys.stdin.readline

c = int(input())

for i in range(c):
    n, *a = list(map(int, input().split()))
    
    v = sum(a) / n
    res = 0
    
    for x in a:
        if x > v:
            res += 1
            
    print(f'{res / n * 100:.3f}%')
    