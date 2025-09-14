n, m = map(int, input().split())
a_elements = set(map(int, input().split()))
b_elements = set(map(int, input().split()))
    
intersection_count = 0
for element in a_elements:
    if element in b_elements:
        intersection_count += 1
            
symmetric_difference_count = (n + m) - 2 * intersection_count
    
print(symmetric_difference_count)