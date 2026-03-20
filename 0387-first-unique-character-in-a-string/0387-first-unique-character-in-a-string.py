class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = [0] * 26
        for char in s:
            chars[ord(char) - ord('a')] += 1

        for i, char in enumerate(s):
            if chars[ord(char) - ord('a')] == 1:
                return i
        return -1