a = int(input())
b = int(input())
c = int(input())

angles = [a, b, c]
total = sum(angles)
set_angles = set(angles)

if total != 180:
    print("Error")
elif len(set_angles) == 1:
    print("Equilateral")
elif len(set_angles) == 2:
    print("Isosceles")
else:
    print("Scalene")