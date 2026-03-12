class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sChars = defaultdict(int)
        tChars = defaultdict(int)

        for char in s:
            sChars[char] += 1
        
        for char in t:
            if char not in sChars:
                return char
            tChars[char] += 1
            if tChars[char] > sChars[char]:
                return char