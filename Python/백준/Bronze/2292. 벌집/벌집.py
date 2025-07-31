n = int(input())

cnt = 1
end = 1

while end < n:
    end += 6 * cnt
    cnt += 1
    
print(cnt)