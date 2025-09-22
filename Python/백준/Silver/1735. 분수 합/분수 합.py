import math

# 첫 번째 분수
A, B = map(int, input().split())
# 두 번째 분수
C, D = map(int, input().split())

# 분자와 분모
numer = A * D + C * B
denom = B * D

# 최대공약수
g = math.gcd(numer, denom)

# 기약분수
print(numer // g, denom // g)
