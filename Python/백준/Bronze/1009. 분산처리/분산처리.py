T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    a %= 10
    if a == 0:
        print(10)
        continue

    pattern = []
    temp = a
    while temp not in pattern:
        pattern.append(temp)
        temp = (temp * a) % 10

    result = pattern[(b - 1) % len(pattern)]
    print(result)
