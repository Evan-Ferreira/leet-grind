class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7 
        remainder = n % 7

        res = 21 * weeks
        for i in range(1, weeks + 1):
            res += i * 7
        
        if remainder:
            res += (weeks + 1) * remainder
            for i in range(1, remainder):
                res += i

        return res


