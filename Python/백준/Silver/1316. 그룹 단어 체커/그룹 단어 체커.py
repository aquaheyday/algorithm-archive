n = int(input())
total = 0

for _ in range(n):
    word = input()
    seen = set()
    prev = ""
    
    is_group = True
    
    for ch in word:
        if ch != prev:
            if ch in seen:
                is_group = False
                break
            seen.add(ch)
        prev = ch
        
    if is_group:
        total += 1
        
print(total)
            