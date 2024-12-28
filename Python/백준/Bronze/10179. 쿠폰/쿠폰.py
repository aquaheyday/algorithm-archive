import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    a = float(input())
    
    print(f'${(a * .8):.2f}')