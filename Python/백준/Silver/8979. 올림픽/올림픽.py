import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = []
res = 1

# 대상 국가 k 찾기
for i in range(n):
    if a[i][0] == k:  # 국가 번호가 k인 국가 찾기
        b = a[i]
        break

# 순위 계산
for i in range(n):
    if a[i][1] > b[1]:  # 금메달 비교
        res += 1
    elif a[i][1] == b[1] and a[i][2] > b[2]:  # 은메달 비교
        res += 1
    elif a[i][1] == b[1] and a[i][2] == b[2] and a[i][3] > b[3]:  # 동메달 비교
        res += 1

print(res)
