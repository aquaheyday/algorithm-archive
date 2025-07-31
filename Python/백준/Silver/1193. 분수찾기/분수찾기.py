n = int(input())

line = 1

while n > line * (line + 1) // 2:
    line += 1
    
prev_sum = (line - 1) * line // 2
pos = n - prev_sum

if line % 2 == 1:
    numerator = line - (pos - 1)
    denominator = pos
else:
    numerator = pos
    denominator = line - (pos - 1)

print(f"{numerator}/{denominator}")