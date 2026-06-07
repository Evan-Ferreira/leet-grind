class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False
        nums.sort(reverse=True)
        target = sum(nums) / k
        used = [False] * len(nums)

        def backtrack(i, k, curr):
            if k == 0:
                return True
            
            if curr == target:
                return backtrack(0, k - 1, 0)
            
            for j in range(i, len(nums)):
                if used[j] or target < (nums[j] + curr):
                    continue
                
                used[j] = True
                if backtrack(j + 1, k, curr + nums[j]):
                    return True
                used[j] = False

                if curr == 0:
                    return False
            return False
        return backtrack(0, k, 0)