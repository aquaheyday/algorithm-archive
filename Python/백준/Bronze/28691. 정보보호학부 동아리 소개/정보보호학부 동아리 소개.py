import sys
input = sys.stdin.readline

d = {
    'M': 'MatKor', 'W': 'WiCys', 'C': 'CyKor', 'A': 'AlKor', '$': '$clear'
}

a = input().rstrip()

print(d[a])