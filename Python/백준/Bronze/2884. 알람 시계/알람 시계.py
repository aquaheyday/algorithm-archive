h, m = map(int, input().split())

if m - 45 < 0:
    rm = 60 - (45 - m)
    if h == 0:
        rh = 23
    else:
        rh = h - 1
else:
    rh = h
    rm = m - 45
    
print(rh,rm)
    
