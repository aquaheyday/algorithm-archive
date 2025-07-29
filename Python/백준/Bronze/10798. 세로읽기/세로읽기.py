max_len = 0
word = []

for _ in range(5):
    ch = input()
    word.append(ch)
    
    if max_len < len(ch):
        max_len = len(ch)
        
for i in range(max_len):
    for j in range(5):
        if i < len(word[j]):
            print(word[j][i], end="")
        