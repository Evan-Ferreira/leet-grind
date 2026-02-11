class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        swap1 = swap2 = swaps = 0

        for i in range(len(s1)):
            if s1[i] != s2[i] and swaps >= 2:
                return False
            elif s1[i] != s2[i] and swaps == 0:
                swap1 = i
                swaps += 1
            elif s1[i] != s2[i] and swaps == 1:
                swap2 = i
                swaps += 1
            else:
                continue
        if swaps == 0:
            return True
        if swaps == 1:
            return False
        newS1 = s1[:swap1] + s1[swap2] + s1[swap1 + 1:swap2] + s1[swap1] + s2[swap2 + 1:]
        return newS1 == s2

        
        
