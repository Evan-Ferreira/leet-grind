class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join('0' if n[i] == '1' else '1' for i, n in enumerate(nums))


            
            
            

            
