import sys
input = sys.stdin.readline

mbti = input().rstrip()
n = int(input())
cnt = 0

for i in range(n):
    mbti2 = input().rstrip()
    
    if mbti == mbti2:
        cnt += 1
        
print(cnt)