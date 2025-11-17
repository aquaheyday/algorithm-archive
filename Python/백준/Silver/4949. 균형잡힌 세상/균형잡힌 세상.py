while True:
    s = input()
    if s == ".":   # 종료 조건
        break
    
    stack = []
    balanced = True

    for ch in s:
        if ch in '([':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack[-1] != '(':
                balanced = False
                break
            stack.pop()
        elif ch == ']':
            if not stack or stack[-1] != '[':
                balanced = False
                break
            stack.pop()

    if balanced and not stack:
        print("yes")
    else:
        print("no")
