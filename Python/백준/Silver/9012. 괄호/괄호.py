import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    s = deque()
    PS = input().rstrip()
    answer = 'YES' # 일단 answer을 YES 로 기록해둠
    for x in PS:
        if x == '(': # ( -> 스택에 추가
            s.append(x)
        elif x == ')':
            if len(s) == 0: # 빈 스택이면 짝 안 맞음 -> answer = 'NO'
                answer = 'NO'
                break
            else: # 빈 스택 아니면 스택 맨 위 요소 pop
                s.pop()
    if len(s) != 0: # 다 돌았는데 빈 스택이 아님 -> 짝 안 맞음 -> answer = 'NO'
        answer = 'NO'
    print(answer)