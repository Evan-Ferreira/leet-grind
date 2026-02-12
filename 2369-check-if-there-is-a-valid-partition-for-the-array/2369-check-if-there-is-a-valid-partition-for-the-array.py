class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        m = {}
        def dfs(i):
            if i >= len(nums):
                m[i] = True
                return True
            if i in m:
                return m[i]
            if (i + 1) < len(nums) and nums[i] == nums[i + 1]:
                res = dfs(i + 2)
                if res:
                    m[i] = True
                    return True
                else: 
                    m[i] = False
                return m[i]
            if (i + 2) < len(nums) and nums[i] == nums[i + 1] == nums[i + 2]:
                res = dfs(i + 3)
                if res:
                    m[i] = True
                    return True
                else: 
                    m[i] = False
                return m[i]
            if (i + 2) < len(nums) and (nums[i] + 2) == (nums[i + 1] + 1) == (nums[i + 2]):
                res = dfs(i + 3)
                if res:
                    m[i] = True
                    return True
                else: 
                    m[i] = False
                return m[i]
            m[i] = False
            return False
        return dfs(0)
            

