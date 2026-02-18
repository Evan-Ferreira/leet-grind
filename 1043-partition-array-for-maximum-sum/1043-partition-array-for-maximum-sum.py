class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            res = 0
            curr_max = 0
            for j in range(i, min(len(arr), i + k)):
                window_size = j - i + 1
                curr_max = max(curr_max, arr[j])
                res = max(res, dfs(j + 1) + window_size * curr_max)
            
            cache[i] = res
            return res
        return dfs(0)
