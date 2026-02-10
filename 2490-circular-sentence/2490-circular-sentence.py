class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split()
        prevLastChar = s[0][-1]
        
        for word in s[1:]:
            currFirstChar = word[0]
            if currFirstChar != prevLastChar:
                return False
            prevLastChar = word[-1]
        prevLastChar = s[-1][-1]
        currFirstChar = s[0][0]
        if prevLastChar != currFirstChar:
            return False
        return True
