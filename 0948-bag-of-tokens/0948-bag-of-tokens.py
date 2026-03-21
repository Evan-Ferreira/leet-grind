class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()

        l, r = 0, len(tokens) - 1
        score = res = 0

        if not tokens or tokens[l] > power:
            return 0

        while l <= r:
            if tokens[l] <= power:
                power -= tokens[l]
                score += 1
                l += 1
            else:
                power += tokens[r]
                score -= 1
                r -= 1
            res = max(score, res)
        
        return res