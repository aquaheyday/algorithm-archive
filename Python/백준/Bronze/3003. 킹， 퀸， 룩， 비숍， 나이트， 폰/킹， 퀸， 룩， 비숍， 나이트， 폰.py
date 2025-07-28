checked = [1,1,2,2,2,8]
result = []

n = list(map(int, input().split()))


for i, v in enumerate(checked):
    result.append(v - n[i])

print(*result)