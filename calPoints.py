def calPoints(operations: list[str]) -> int:
        stack = []
        for val in operations:
            if val == 'D':
                stack.append(stack[-1] * 2)
            elif val == 'C':
                stack.pop()
            elif val == '+':
                val1 = stack[len(stack) - 2]
                val2 = stack[-1]
                stack.append(val1 + val2)
            else:
                stack.append(int(val))

        
        return sum(stack)
ops = ["5","-2","4","C","D","9","+","+"]
calPoints(ops)