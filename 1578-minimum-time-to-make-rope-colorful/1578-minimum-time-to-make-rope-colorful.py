class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        N = len(colors)
        i = 1
        res = 0
        stack = []
        while i < N:
            curr = currMax = neededTime[i - 1]
            while i < N and colors[i] == colors[i - 1]:
                curr += neededTime[i]
                currMax = max(currMax, neededTime[i])
                i += 1
            if curr:
                res += curr - currMax
            i += 1
        return res

