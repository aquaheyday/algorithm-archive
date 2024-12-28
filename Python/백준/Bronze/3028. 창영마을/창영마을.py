import sys
input = sys.stdin.readline

a = input().rstrip()
b = 1

for i in a:
    if i == 'A' and b != 3:
        b = 3 - b
    elif i == 'B' and b != 1:
        b = 5 - b
    elif i == 'C' and b != 2:
        b = 4 - b
        
print(b)
        
        