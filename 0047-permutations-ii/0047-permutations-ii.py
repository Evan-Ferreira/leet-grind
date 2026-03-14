class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        nMap = defaultdict(int)
        nUsed = len(nums)
        for n in nums:
            nMap[n] += 1

        def backtrack():
            nonlocal nUsed
            if nUsed == 0:
                res.append(curr.copy())
                return
            
            for key, val in nMap.items():
                if val == 0:
                    continue
                
                nUsed -= 1
                curr.append(key)
                nMap[key] -= 1
                backtrack()
                curr.pop()
                nMap[key] += 1
                nUsed += 1
        
        backtrack()
        return res