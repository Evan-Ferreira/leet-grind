class Solution:
    def reverseParentheses(self, s: str) -> str:
        N = len(s)
        stack = []
        link = [0] * N
        res = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                link[i] = j
                link[j] = i
        
        dr, i = 1, 0
        while i < N:
            if s[i].isalpha():
                res.append(s[i])
            else:
                i = link[i]
                dr = -dr
            i += dr
        return "".join(res)
