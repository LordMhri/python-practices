def simplifyPath(path:str) -> str:
    stack = []
    paths = path.split("/")
    for pa in paths:
        if pa == '' or pa == '.':
            pass
        elif pa == '..':
            if len(stack) != 0:
                stack.pop()
        else:
            stack.append(pa)

    return '/' + "/".join(stack)
    
paths = "/../"

print(simplifyPath(paths))