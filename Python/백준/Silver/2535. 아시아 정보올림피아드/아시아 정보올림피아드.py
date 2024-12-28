import sys
input = sys.stdin.readline

n = int(input())
participants = [list(map(int, input().split())) for _ in range(n)]
participants.sort(key=lambda x: -x[2])


selected = []
country_count = {}

for participant in participants:
    country, student, score = participant

    if country_count.get(country, 0) >= 2:
        continue

    selected.append((country, student))
    country_count[country] = country_count.get(country, 0) + 1

    if len(selected) == 3:
        break

for country, student in selected:
    print(country, student)
