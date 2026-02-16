class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        m = defaultdict(int)
        for char in s:
            m[char] += 1
        
        odd = 0
        for n in m.values():
            if n % 2 != 0:
                odd += 1
        print(odd)
        if len(s) % 2 == 0 and odd > 0:
            return False
        if len(s) % 2 == 1 and odd > 1:
            return False
        return True