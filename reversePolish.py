def evalRPN(tokens: list[str]) -> int:
    operators = {'+', '-', '*', '/'}
    ans = []
    for token in tokens:
        if not ans:
            ans.append(token)
        elif token in operators:
            val1 = ans.pop()
            val2 = ans.pop()
            if token == '+':
                ans.append(int(val2) + int(val1))
            elif token == '-':
                ans.append(int(val2) - int(val1))
            elif token == '*':
                ans.append(int(val2) * int(val1))
            elif token == '/':
                ans.append(int(val2) / int(val1))
        else:
            ans.append(token)
    
    return int(ans[0])