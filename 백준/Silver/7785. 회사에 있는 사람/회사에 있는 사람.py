n = int(input())
log = {}

for _ in range(n):
    name, action = input().split()
    if action == "enter":
        log[name] = True
    else:
        if name in log:
            del log[name]

for name in sorted(log.keys(), reverse=True):
    print(name)