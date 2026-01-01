class Solution:
    def smallestString(self, s: str) -> str:
        res = list(s)
        flip = False
        for i, c in enumerate(s):
            if i == (len(s) - 1) and not flip:
                if c == 'a':   
                    res[i] = 'z'
                else:
                    char = chr(ord(c) - 1)
                    res[i] = char
            if not flip:
                if c == 'a':
                    continue
                else:
                    flip = True
                    char = chr(ord(c) - 1)
                    res[i] = char
            if flip:
                if c == 'a':   
                    return "".join(res)
                char = chr(ord(c) - 1)
                res[i] = char
        return "".join(res)