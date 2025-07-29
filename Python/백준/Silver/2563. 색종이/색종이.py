matrix = [[0] * 100 for _ in range(100)]

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    
    for tx in range(x, x + 10):
        for ty in range(y, y + 10):
            matrix[tx][ty] = 1
        
print(sum(sum(row) for row in matrix))