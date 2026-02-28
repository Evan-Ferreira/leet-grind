class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = [""]
        i = 0
        tmp = ''
        while i < len(path):
            if path[i] == '/':
                if tmp:
                    stack.append(tmp)
                tmp = ''
                while i < len(path) and path[i] == '/':
                    i += 1
            elif i + 1 < len(path) and path[i] == '.' and path[i + 1] == '/' and path[i - 1] == '/':
                i += 1
                if tmp:
                    stack.append(tmp)
                tmp = ''
            elif (i + 2 < len(path) and path[i]  == '.' and path[i + 1] == '.' and 
                path[i + 2] == '/' ) and path[i - 1] == '/':
                if len(stack) > 1:
                    stack.pop()
                i += 2
                tmp = ''
            else:
                tmp += path[i]
                i += 1
        if len(tmp) == 2 and tmp[0] == '.' and tmp[1] == '.' and stack:
            stack.pop()
        elif tmp and not (len(tmp) == 1 and tmp[0] == '.'):
            stack.append(tmp)
        if (len(stack) == 1 and not stack[0]) or not stack:
            return "/"
        return "/".join(stack)