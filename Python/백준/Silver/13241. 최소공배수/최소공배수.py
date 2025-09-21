import math

A, B = map(int, input().split())
g = math.gcd(A, B)
lcm = A * B // g
print(lcm)
