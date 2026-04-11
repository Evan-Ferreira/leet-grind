class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        N = len(potions) 
        res = []

        dp = {}

        def getAmount(spell):
            l, r = 0, N - 1
            while l <= r:
                mid = (l + r) // 2
                product = potions[mid] * spell
                if product > success:
                    r = mid - 1
                elif product < success:
                    l = mid + 1
                else:
                    while mid > 0 and potions[mid] == potions[mid - 1]:
                        mid -= 1
                    return N - mid
            return N - l
        
        for s in spells:
            if s in dp:
                res.append(dp[s])
            else:
                dp[s] = getAmount(s)
                res.append(dp[s])
        
        return res
        

            
