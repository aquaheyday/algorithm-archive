import sys
input = sys.stdin.readline

a = input().rstrip()
d = {
    'NLCS': 'North London Collegiate School',
    'BHA': 'Branksome Hall Asia',
    'KIS': 'Korea International School',
    'SJA': 'St. Johnsbury Academy'
}

print(d[a])