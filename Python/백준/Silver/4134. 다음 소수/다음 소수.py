import sys

# Miller-Rabin 소수 판별법
def is_prime(n):
    if n < 2:
        return False
    # 간단한 소수 체크
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0:
            return n == p

    # n-1 = d * 2^s 형태로 분해
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    # 정확성을 위해 bases 는 충분
    for a in [2, 7, 61]:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def next_prime(n):
    if n <= 2:
        return 2
    if n % 2 == 0:
        n += 1
    while not is_prime(n):
        n += 2
    return n


input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    print(next_prime(n))
