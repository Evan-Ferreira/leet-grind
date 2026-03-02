class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        tI = 0
        for sI in range(len(s)):
            if tI < len(t) and s[sI] != t[tI]:
                while tI < len(t) and s[sI] != t[tI]:
                    tI += 1
                        
            if tI >= len(t):
                return False
            
            if s[sI] == t[tI]:
                tI += 1
        
        return True