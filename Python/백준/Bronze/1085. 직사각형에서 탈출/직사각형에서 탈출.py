x,y,w,h = map(int, input().split())
t = []

t.append(w - x)
t.append(x)
t.append(h - y)
t.append(y)

print(min(t))