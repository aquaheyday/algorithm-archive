import sys
input = sys.stdin.readline

w = []
k = []

wR = 0
kR = 0

for i in range(20):
    n = int(input())
    
    if i < 10:
        w.append(n)
    else:
        k.append(n)

for i in range(3):
    a = max(w)
    w.remove(a)
    wR += a
    
    b = max(k)
    k.remove(b)
    kR += b

print(wR, kR)