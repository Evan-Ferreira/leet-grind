class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        i = 0
        while tickets[k]:
            if tickets[i]:
                res += 1
                tickets[i] -= 1
            i = 0 if i == (len(tickets) - 1) else i + 1
        return res
