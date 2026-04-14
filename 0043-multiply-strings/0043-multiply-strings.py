class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def getInt(num):
            res = 0
            N = len(num)
            for i in range(N - 1, -1, -1):
                char = ord(num[i]) - ord('0')
                res += (char * 10**(N - i - 1))
            return res

        return str(getInt(num1) * getInt(num2))