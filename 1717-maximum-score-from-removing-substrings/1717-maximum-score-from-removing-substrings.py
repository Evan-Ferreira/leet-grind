class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def removePair(pair, score):
            nonlocal s
            res = 0
            stack = []

            for c in s:
                if pair[1] == c and stack and stack[-1] == pair[0]:
                    stack.pop()
                    res += score
                else:
                    stack.append(c)
            s = "".join(stack)
            return res
        
        res = 0
        pair = "ab" if x > y else "ba"
        res += removePair(pair, max(x, y))
        res += removePair(pair[::-1], min(x, y))
        return res