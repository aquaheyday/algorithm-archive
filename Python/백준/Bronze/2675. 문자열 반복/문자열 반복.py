n = int(input())

for _ in range(n):
    r = ""
    i, s = input().split()
    for x in s:
        r += x * int(i)
    print(r) 
       
