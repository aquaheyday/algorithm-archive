import sys

input = sys.stdin.readline

T = int(input())
nums = [int(input()) for _ in range(T)]
MAX_N = max(nums)

# 1) 에라토스테네스의 체
is_prime = [False, False] + [True] * (MAX_N - 1)
for i in range(2, int(MAX_N ** 0.5) + 1):
    if is_prime[i]:
        step = i
        start = i * i
        is_prime[start:MAX_N+1:step] = [False] * (((MAX_N - start) // step) + 1)

# 소수 리스트(카운트 시 순회 용)
primes = [i for i in range(2, MAX_N + 1) if is_prime[i]]

# 2) 각 테스트 케이스 처리
out_lines = []
for N in nums:
    half = N // 2
    cnt = 0
    # p <= N/2 인 소수만 확인
    for p in primes:
        if p > half:
            break
        if is_prime[N - p]:
            cnt += 1
    out_lines.append(str(cnt))

print("\n".join(out_lines))
