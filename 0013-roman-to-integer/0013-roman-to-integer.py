class Solution:
    def romanToInt(self, s: str) -> int:
        syms = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" :500,
            "M" : 1000,
        }
        res = 0
        for r in range(1, len(s)):
            l = r - 1
            if syms[s[r]] > syms[s[l]]:
                res -= syms[s[l]]
            else:
                res += syms[s[l]]
        return res + syms[s[len(s) - 1]]