class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i, char in enumerate(s):
            res += (ord("z") - ord(char) + 1) * (i + 1)
        return res