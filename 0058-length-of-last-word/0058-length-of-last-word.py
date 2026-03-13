class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for w in s.split(' ')[::-1]:
            if len(w) > 0:
                return len(w)