class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        nums = set(nums)
        res = [""]

        for i in range(n):
            seen = set()
            tmpRes = []
            for num in nums:
                seen.add(num[i])
            for j in range(len(res)):
                if len(seen) == 2:
                    tmpRes.append(res[j] + "1")
                    tmpRes.append(res[j] + "0")
                elif "1" in seen:
                    return res[-1] + ("0" * (n - i))
                else:
                    return res[-1] + ("1" * (n - i))
            res = tmpRes
        for n in res:
            if n not in nums:
                return n


            
            
            

            
