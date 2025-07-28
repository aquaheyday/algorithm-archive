words = input()

wc = [0] * 26

for x in words:
    wc[ord(x.lower()) - ord("a")] += 1
    
max_count = max(wc)

if wc.count(max_count) > 1:
    print("?")
else:
    idx = wc.index(max_count)
    print(chr(idx + ord("A"))) 