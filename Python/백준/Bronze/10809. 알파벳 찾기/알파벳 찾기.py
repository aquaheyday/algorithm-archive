a = [-1] * 26

s = input()

for i in range(len(s)):
    idx = ord(s[i]) - ord("a")
    if a[idx] == -1:
        a[idx] = i
    
print(*a)
    
