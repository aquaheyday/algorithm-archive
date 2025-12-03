from collections import deque
import sys

input = sys.stdin.readline

N = int(input().strip())
moves = list(map(int, input().split()))

# (풍선 번호, 이동값)를 덱에 저장
dq = deque((i + 1, moves[i]) for i in range(N))

result = []

# 첫 풍선부터 차례로 터뜨리기
while dq:
    idx, move = dq.popleft()   # 현재 풍선 터뜨림
    result.append(idx)

    if not dq:  # 더 이상 남은 풍선 없으면 끝
        break

    if move > 0:
        # 이미 하나는 터뜨렸으니 move-1만큼 오른쪽 이동
        dq.rotate(-(move - 1))
    else:
        # 음수일 때는 그대로 회전 (왼쪽으로 abs(move)만큼)
        dq.rotate(-move)

print(*result)
