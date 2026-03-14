class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = set()
        res = set()
        curr = []

        def backtrack():
            if len(used) == len(nums):
                res.add(tuple(curr.copy()))
                return
            
            for i in range(len(nums)):
                if i in used:
                    continue
                
                curr.append(nums[i])
                used.add(i)
                backtrack()
                used.remove(i)
                curr.pop()
        
        backtrack()
        return list(res)