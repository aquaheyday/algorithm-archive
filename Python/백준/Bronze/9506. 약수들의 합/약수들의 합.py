while True:
    
    n = int(input())
    r = []
    
    if n == -1:
        break

    for i in range(1, n):
        if n % i == 0:
            r.append(i)
        
    if sum(r) == n:
        print(f"{n} = {' + '.join(map(str, r))}")
    else:
        print(f"{n} is NOT perfect.")