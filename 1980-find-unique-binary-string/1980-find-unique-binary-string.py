class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        nums = set(nums)


        def dfs(curr):
            if len(curr) == n and curr not in nums:
                return curr
            
            if len(curr) == n:
                return ""
            
            ans1 = dfs(curr + "1")
            ans0 = dfs(curr + "0")
            if ans1:
                return ans1
            return ans0
        
        return dfs("")
            
            
            

            
