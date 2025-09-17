import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 번호로 이름 조회 (1-based)
names = [None] * (N + 1)
# 이름으로 번호 조회
name_to_idx = {}

for i in range(1, N + 1):
    s = input().strip()
    names[i] = s
    name_to_idx[s] = str(i)   # 출력시 바로 쓰기 위해 문자열로 저장

out = []
for _ in range(M):
    q = input().strip()
    if q.isdigit():
        out.append(names[int(q)])
    else:
        out.append(name_to_idx[q])

print("\n".join(out))
