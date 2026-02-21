class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            res = 0
            while n:
                res += (n % 10) ** 2
                n = n // 10
            if res in seen:
                return False
            seen.add(res)
            n = res
        return True
