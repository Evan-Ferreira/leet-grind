class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_map = defaultdict(int)

        for num in arr1:
            arr1_map[num] += 1
        
        res = []
        for num in arr2:
            res += [num] * arr1_map[num]
            del arr1_map[num]
        
        remaining_keys = sorted(arr1_map.keys())
        for key in remaining_keys:
            res += [key] * arr1_map[key]
            del arr1_map[key]

        return res
