class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        maxValue = tickets[k]
        for i, t in enumerate(tickets):
            if i <= k:
                res += min(t, maxValue)
            else:
                res += min(t, maxValue - 1)
        return res
