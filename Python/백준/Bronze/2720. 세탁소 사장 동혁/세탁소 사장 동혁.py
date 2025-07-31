n = int(input())

for _ in range(n):
    cost = int(input())
    
    quarters = cost // 25
    cost %= 25
    
    dime = cost // 10
    cost %= 10
    
    nickel = cost // 5
    cost %= 5
    
    penny = cost // 1
    
    print(quarters, dime, nickel, penny)