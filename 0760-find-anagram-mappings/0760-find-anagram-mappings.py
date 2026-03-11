class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mem = {}
        for i, n in enumerate(nums2):
            mem[n] = i
        
        return [mem[n] for n in nums1]
