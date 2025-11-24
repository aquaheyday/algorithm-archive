import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))

stack = []
order = 1  # 1번부터 차례대로 나가야 함

for x in line:
    # 먼저 스택 top 이 나가야 하는 경우 처리
    while stack and stack[-1] == order:
        stack.pop()
        order += 1

    if x == order:
        order += 1
    else:
        stack.append(x)

# 남아있는 stack 처리
while stack and stack[-1] == order:
    stack.pop()
    order += 1

# 최종 판별
if order == n + 1:
    print("Nice")
else:
    print("Sad")
