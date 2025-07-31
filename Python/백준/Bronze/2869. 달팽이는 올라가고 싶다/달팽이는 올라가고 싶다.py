import math

a, b, v = map(int, input().split())

if a >= v:
    day = 1
else:
    day = math.ceil((v - a) / (a - b)) + 1
    
print(day)