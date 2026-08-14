class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res = l = 0 
        seen = [0] * 26
        for r in range(len(s)):
            r_index = ord(s[r]) - ord('a')
            seen[r_index] += 1
            while seen[r_index] > 2:
                l_index = ord(s[l]) - ord('a')
                seen[l_index] = max(seen[l_index] - 1, 0)
                l += 1
            res = max(r - l + 1, res)
        return res
            
            
